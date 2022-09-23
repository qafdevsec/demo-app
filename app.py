from app import app, api, jwt
import config
from app.blacklist import BLACKLIST
from app.resources.users import Users, UserLogin, UserByEmail
from flask import jsonify, render_template





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
