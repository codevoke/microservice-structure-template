import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from API import api, db_init_app


app = Flask(__name__)
CORS(app)

# create jwt manager object for configuring app with jwt
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

# configure database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DEVELOPMENT_DATABASE_URI')  # PRODUCTION_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
# init flask app to db
db_init_app(app)

# initialization app to api
api.init_app(app)
