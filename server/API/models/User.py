from .db import db, BaseModel
from passlib.hash import pbkdf2_sha256


class UserModel(BaseModel): 
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # other fields here

    @classmethod
    def auth(cls, username, password):
        user = cls.query.filter_by(username=username).first()
        if user is None:
            raise UserExceptions.UserNotFound
        if pbkdf2_sha256.verify(password, user.password):
            return user
        else:
            raise UserExceptions.InvalidPassword


class UserExceptions:
    class UserNotFound(Exception):
        pass
    class InvalidPassword(Exception):
        pass
