
import flask
import ldap3

blueprint = flask.Blueprint('auth', __name__)

LDAP_IP = 'ldap://127.0.0.1:389'

def connection_conf(email, prefix='cn'): 
    return '{}={},dc=dexter,dc=com,dc=br'.format(prefix, email)

def connection_conf_email(email): 
    return connection_conf(email, prefix='uid')

def get_connection():
    return ldap3.Connection(
        ldap3.Server(LDAP_IP),
        connection_conf('admin'),
        '4linux'
    )


@blueprint.route('/sign-in', methods=[ 'GET' ])
def get_sign_in():    
    context = {
        'page': 'sign-in',
        'route': {
            'is_public': True
        },
    }
    return flask.render_template('sign-in.html', context=context)


@blueprint.route('/sign-in', methods=[ 'POST' ])
def post_sign_in():
    connection = get_connection()
    try:
        connection.bind()
    except:
        flask.flash('Sem conexão como LDAP', 'danger')
        return flask.redirect('/sign-in')

    email = flask.request.form['email']
    password = flask.request.form['password']

    connection.search(
        connection_conf_email(email),
        '(objectClass=person)', 
        attributes=['userPassword',]
    )
    try:
        saved_password = connection.entries[0].\
            userPassword.value.decode()

        if saved_password == password:
            flask.flash('Seja Bem-vindo', 'success')
            flask.session['email'] = email
            return flask.redirect('/')

        raise Exception('')
    except:
        flask.flash('Usuário não encontrado no LDAP', 'danger')
        return flask.redirect('/sign-in')


@blueprint.route('/sign-up', methods=[ 'GET', 'POST' ])
def get_sign_up():    

    if flask.request.method == 'POST':
        connection = get_connection()
        try:
            connection.bind()
        except:
            flask.flash('Sem conexão como LDAP', 'danger')
            return flask.redirect('/sign-up')
        
        first_name = flask.request.form['first_name']
        last_name = flask.request.form['last_name']
        email = flask.request.form['email']
        password = flask.request.form['password']
        object_class = [
            'top',
            'person',
            'organizationalPerson',
            'inetOrgPerson'
        ]
        user = {
            'cn': first_name,
            'sn': last_name,
            'mail': email,
            'uid': email,
            'userPassword': password
        }
        print(connection_conf_email(email))
        if connection.add(connection_conf_email(email), object_class, user):
            flask.flash('Usuário Cadastrado com sucesso', 'success')
            return flask.redirect('/sign-in')
                    
        flask.flash('Erro ao cadastrar usuário', 'danger')

    context = {
        'page': 'sign-up',
        'route': {
            'is_public': True
        },
    }

    return flask.render_template('sign-up.html', context=context)



@blueprint.route('/sign-out', methods=[ 'POST' ])
def post_sign_out():
    if 'email' in flask.session:
        del flask.session['email']
        return flask.redirect('/sign-in')
    
    return flask.redirect('/')
    