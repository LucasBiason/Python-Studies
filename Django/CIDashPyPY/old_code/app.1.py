import flask
import pymongo

client = pymongo.MongoClient()
db = client.users

app = flask.Flask(__name__)

IS_AUTH = False

@app.route('users/sign-in', methods=['GET', 'POST'])
def sign_in():
    if flask.request.method == 'POST':
        form = flask.request.form
        user = db.usuarios.find({'email':form['email']})
        if not user:
            return 'Usuário não encontrado'

        if form['password'] == user['password']:
            IS_AUTH = True
            return flask.redirect('/dashboard')
        
    return flask.render_template('sign-in.html')

@app.route('users/sign-up', methods=['POST'])
def sign_up():
    form = flask.request.form
    
    for user in db.usuarios.find():
        if form['email'] == user['email']:
            if form['password'] == user['password']:
                return 'usuário já existente'
    
    db.usuarios.insert(form)
    return flask.redirect('/home')

@app.route('users/sign-out', methods=['POST'])
def sign_out():
    pass

if __name__ == '__main__':
    app.run(debug=True)