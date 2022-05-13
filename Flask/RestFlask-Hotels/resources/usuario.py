from flask_restful import Resource, reqparse
from models import UserModel


class Usuario(Resource):

    def get(self, user_id):
        Usuario = UserModel.get_or_none(user_id)
        if Usuario:
            return Usuario.serialize(), 200
        return {'message': 'User not found.'}, 401

    def delete(self, user_id):
        usuario = UserModel.get_or_none(user_id)
        if not usuario:
            return {'message': f'User id {user_id} not found.'}, 401
        try:
            usuario.remove()
        except Exception:
            return {'message': 'An error ocurred tryint to delete user.'}, 500
        return {'message': 'User deleted.'}, 200


class UserRequestParser():
    atributos = reqparse.RequestParser()
    atributos.add_argument('login', type=str, required=True, help="The field 'login' connot be blank.")
    atributos.add_argument('password', type=str, required=True, help="The field 'password' connot be blank.")


class UserRegister(Resource, UserRequestParser):
    # /register
    def post(self):
        dados = self.atributos.parse_args()

        if UserModel.get_by_login(dados.get('login')):
            return {
                "message": f'The login {dados.get("login")} already exists'
            }, 401

        user = UserModel.perform_save(**dados)
        return {"message": "User created successfully!"}, 201



class UserLogin(Resource, UserRequestParser):
    # /login
    def post(self):
        dados = self.atributos.parse_args()

        if not UserModel.get_by_login(dados.get('login')):
            return {"message": f'User not found'}, 401

        user = UserModel.authenticate(**dados)
        return {}, 201