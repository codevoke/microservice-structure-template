from http import HTTPStatus

from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token

from models import exceptions as exc
from server.API.models import User

ENDPOINT = "/auth"


class Auth(Resource):
    path = ENDPOINT

    @classmethod
    def post(cls):
        args = request.get_json()
    
        try:
            user = User.auth(args["username"], args["password"])
        except exc.UserNotFound:
            return {"message": "user not found by that username"}, HTTPStatus.NOT_FOUND
        except exc.InvalidPassword:
            return {"message": "invalid password"}, HTTPStatus.UNAUTHORIZED

        return {"access_token": create_access_token(identity=user.id)}, HTTPStatus.OK
