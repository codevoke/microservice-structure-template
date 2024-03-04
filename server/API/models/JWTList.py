from .db import db, BaseModel


class JWTList(BaseModel):
    __tablename__ = "jwt_list"

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    jti = db.Column(db.String(36), nullable=False, primary_key=True)
    is_blocked = db.Column(db.Boolean, default=False, nullable=False)

    def block(self):
        self.is_blocked = True

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
    
    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()
    
    @classmethod
    def get_by_jti(cls, jti):
        jwt = cls.query.filter_by(jti=jti).first()
        if jwt is None: 
            raise JWTExceptions.JWTNotFound
        return jwt

    @classmethod
    def block_all_tokens(cls, user_id):
        tokens = cls.get_by_user_id(user_id)
        for token in tokens:
            token.block()


class JWTExceptions:
    class JWTNotFound(Exception):
        pass
