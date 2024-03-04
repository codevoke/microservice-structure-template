from flask_restful import Api
from flask_jwt_extended import JWTManager

from .resources import resource_list
from .models import JWTBlocklist, db_init_app


api = Api(prefix="/api")

for resource in resource_list:
    api.add_resource(resource, resource.path)

# configure jwt
JWT = JWTManager()

@JWT.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return JWTBlocklist.is_jti_blacklisted(jti)
