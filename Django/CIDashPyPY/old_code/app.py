import flask

USUARIO_LOGADO = {
    'email': 'teste@teste',
    'password': '123'
}

app = flask.Flask(__name__)

@app.route('/')
def get_index():
    return flask.render_template('index.html')
    
@app.route('/sign-in', methods=['POST'])
def sign_in():
    form = flask.request.form

    if form['email'] == USUARIO_LOGADO['email']:
        if form['password'] == USUARIO_LOGADO['password']:
            return flask.redirect('/dashboard')

    return flask.redirect('/')

@app.route('/dashboard')
def dashboard():
    return flask.render_template('dashboard.html')

@app.route('/users')
def get_users():
    pass

if __name__ == '__main__':
    app.run(debug=True)