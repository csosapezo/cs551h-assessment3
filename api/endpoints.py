"API endpoint definition"

from flask import Blueprint
from flask_restful import Api

from api.getplayer import GetPlayer
from api.demo import Demo

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

api.add_resource(Demo, '/demo/')

api.add_resource(GetPlayer, '/getplayer/')
