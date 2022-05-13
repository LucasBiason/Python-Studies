from flask import Flask
from flask_restful import Api
from resources import hotel, usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Se True, sobrecarrega pois fica rastreando modificações de banco

api = Api(app)

@app.before_first_request
def cria_banco():
    db.create_all()

api.add_resource(hotel.Hoteis, '/hoteis/')
api.add_resource(hotel.Hotel, '/hoteis/<string:hotel_id>/')
api.add_resource(usuario.Usuario, '/users/<string:user_id>/')
api.add_resource(usuario.UserRegister, '/register/')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)
