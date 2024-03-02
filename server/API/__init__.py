from flask_restful import Api
from resources import resources_list


api = Api(prefix="/api")

for resource in resources_list:
    api.add_resource(resource, resource.path)
