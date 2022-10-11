import os
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import datetime, timedelta

import subprocess

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'plkf124Fas4'
app.config['JWT_SECRET_KEY'] = 'plkf124Fas4'
app.config['JWT_BLACKLIST_ENABLED'] = True
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Pswd123$@db1.cdlikiuniwlk.sa-east-1.rds.amazonaws.com/db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://db:mysecret@db1.cdlikiuniwlk.sa-east-1.rds.amazonaws.com/db'

# app.config.update(
#     SESSION_COOKIE_SECURE=True,
#     SESSION_COOKIE_HTTPONLY=True,
#     SESSION_COOKIE_SAMESITE='Lax',
# )


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def dbCreate():
    db.create_all()

api = Api(app)
jwt = JWTManager(app)

db = SQLAlchemy(app)
Migrate(app,db)

CORS(app)

########################################
# LOGIN CONFIGS

login_manager.init_app(app)
login_manager.login_view = "users.login"

# @app.after_request
# def after_request(response):
# #   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
# #   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
# #   response.headers.add('X-Frame-Options', 'SAMEORIGIN')
# #   response.headers.add('X-Content-Type-Options', 'nosniff')
# #   response.headers.add('X-XSS-Protection', '1; mode=block')
# #   response.headers['X-XSS-Protection'] = '1; mode=block'

#   response.headers.add('Content-Security-Policy', "script-src 'self' code.jquery.com cdnjs.cloudflare.com maxcdn.bootstrapcdn.com")
#   return response

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/flaw", methods=["GET","POST"])
def get_email1():
    temp = ""
    if request.method == "GET":

        return render_template("about.html",data=temp)

    if request.method == "POST":
        if request.form.get("email"):
            emailurl = request.form.get("email")
            print(emailurl)
            email =  request.form.get("email") + " has succesfully subscribed to APPsecengineer"
            process = subprocess.Popen(['curl', str(emailurl)], stdout=subprocess.PIPE)
            temp = process.communicate()[0]
        else:
            print("Empty string")
            temp =  "please enter valid E-mail Address"


        return render_template("about.html",data=temp)

from app.users.views import users

app.register_blueprint(users, url_prefix="/users")


### API Routes
from app.resources.users import Users, UserLogin, UserByEmail

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'You have been logged out.'}), 401 # unauthorized

api.add_resource(Users, '/api/users')
api.add_resource(UserLogin, '/api/login')
api.add_resource(UserByEmail, '/api/users/email/<string:email>')