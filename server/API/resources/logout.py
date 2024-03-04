from http import HTTPStatus

from flask_restful import Resource
from flask_jwt_extended import get_jwt, get_jwt_identity, jwt_required

from API.models import DBExceptions as exc
from API.models import JWTList

ENDPOINTS = [
    "/logout", 
    "/logout-all"
]


class Logout(Resource):
    path = ENDPOINTS[0]

    @classmethod
    @jwt_required()
    def post(cls):
        jti = get_jwt()["jti"]
        try:
            JWTList.get_by_jti(jti).block()
        except exc.JWTNotFound:
            return {"message": "invalid token"}, HTTPStatus.UNAUTHORIZED
        return {"message": "successfully logged out"}, HTTPStatus.OK


class LogoutAll(Resource):
    path = ENDPOINTS[1]

    @classmethod
    @jwt_required()
    def post(cls):
        user_id = get_jwt_identity()
        try:
            JWTList.block_all_tokens(user_id)
        except exc.JWTNotFound:
            return {"message": "invalid token"}, HTTPStatus.UNAUTHORIZED
        return {"message": "successfully logged out"}, HTTPStatus.OK
