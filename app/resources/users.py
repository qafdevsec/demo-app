from app import db
from flask import jsonify
from flask_restful import Resource, reqparse
from app.users.model import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from werkzeug.security import check_password_hash, generate_password_hash
from app.blacklist import BLACKLIST 
from datetime import datetime, timedelta


atributos = reqparse.RequestParser()
atributos.add_argument('email', type=str, required=True, help="The field 'email' cannot be left blank.")
atributos.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank.")
atributos.add_argument('name', type=str)
atributos.add_argument('phone', type=str)
atributos.add_argument('admin', type=bool)

updateUserAttributes = reqparse.RequestParser()
updateUserAttributes.add_argument('email', type=str, required=True, help="The field 'email' cannot be left blank.")
updateUserAttributes.add_argument('name', type=str)
updateUserAttributes.add_argument('admin', type=bool)


class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        # print(dados)
        user = User.find_by_email(dados['email'])
        print(user['password'])
        # ok = check_password_hash(user['password'], dados['password'])
        # print(ok)
        if user and check_password_hash(user['password'], dados['password']):

            token_de_accesso = create_access_token(identity=user['email'], fresh=True)
            refresh_token = create_refresh_token(identity=user['email'])
            return {'access_token': token_de_accesso, 'refresh_token': refresh_token, "user": user['email']}, 200
        return {'message': 'The username or password is incorrect.'}, 401 # Unauthorized

class Users(Resource):
    @jwt_required()
    def get(self):
        users = User.query.all()
        return [user.json() for user in users]

class UserByEmail(Resource):
    @jwt_required()
    def get(self, email):

        user = User.query.filter_by(email=email).first()
        if user:
            return [user.json()]