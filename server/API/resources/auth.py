from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from models import exceptions as exc
from models import UserModel

ENDPOINT = "/auth"


class Auth(Resource):
    @classmethod
    def post(cls):
        args = request.get_json()
    
        try:
            user = UserModel.auth(args["username"], args["password"])
        except exc.UserNotFound:
            return {"message": "user not found by that username"}, 404
        except exc.InvalidPassword:
            return {"message": "invalid password"}, 401

        return {"access_token": str(create_access_token(identity=user.id))}