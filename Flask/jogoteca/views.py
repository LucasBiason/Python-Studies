import flask, time

from models import Jogo, Usuario
from decorators import login_required

from main import db, app


@app.route('/')
@login_required
def listagem():
    context = {
        'titulo': 'Jogos',
        'lista_jogos':  Jogo.get_jogos(db)
    }
    return flask.render_template( 'lista.html', ** context)
    

@app.route('/novo', methods=['GET', 'POST' ])
@login_required
def cadastro():
    context = {
        'titulo': 'Jogos - Cadastro',
        'jogo': None,
        'capa_jogo': '',
        'timestamp':''
    }
    
    if flask.request.method == 'POST':
        id =  flask.request.form.get('id')
        nome =  flask.request.form.get('nome')
        categoria =  flask.request.form.get('categoria')
        console =  flask.request.form.get('console')
        jogo = Jogo(nome, categoria, console, id=id)
        Jogo.salvar(db, jogo)
            
        arquivo =  flask.request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        arquivo.save(f'{upload_path}/capa{jogo.id}.jpg')
    
        flask.flash(
            f'Jogo {jogo.nome} salvo com sucesso.',
            'success'
        )
        return flask.redirect('/')
        
    return flask.render_template(
        'novo.html', ** context
    )


@app.route('/editar/<int:id>', methods=['GET', 'POST' ])
@login_required
def editar(id):
    jogo = Jogo.busca_por_id(db, id)
    context = {
        'titulo': 'Jogos - Editando jogo',
        'jogo': jogo,
        'capa_jogo': f'capa{id}.jpg',
        'timestamp': time.time()
    }    
    return flask.render_template('novo.html', ** context)

@app.route('/deletar/<int:id>')
def deletar(id):
    Jogo.deletar(db, id)
    flask.flash('O jogo foi removido com sucesso!', 'success')
    return flask.redirect( flask.url_for('listagem'))
    

@app.route('/uploads/')    
@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo=None):
    default = 'capa_padrao.jpg'
    if not nome_arquivo:
        nome_arquivo =default
    try:
        return flask.send_from_directory('uploads', nome_arquivo)
    except:
        return flask.send_from_directory('uploads', default)


@app.route('/login')
def login():
    proxima = flask.request.args.get('proxima', '')
    return flask.render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    status, retorno = Usuario.autenticar(
        db,
        flask.request.form['usuario'],
        flask.request.form['senha']         
    )
    if status:
        flask.flash(retorno.nome + ' logou com sucesso!', 'success')
        proxima_pagina =  flask.request.form.get('proxima', '')
        flask.session['usuario_logado'] = retorno.id
        print("proxima_pagina: ", proxima_pagina)
        return  flask.redirect('/' if not proxima_pagina else proxima_pagina)
    
    flask.flash(retorno, 'danger')
    return  flask.redirect (flask.url_for('login'))
        

@app.route('/logout')
def logout():
    flask.session['usuario_logado'] = None
    return flask.redirect(flask.url_for('login'))
