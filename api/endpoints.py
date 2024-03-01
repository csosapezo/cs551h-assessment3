"API endpoint definition"

from flask import Blueprint
from flask_restful import Api

from api.getplayer import GetPlayer
from api.demo import Demo
from api.home import Home, PlayerData


blueprint = Blueprint('api', __name__)
api = Api(blueprint)

home_bp = Blueprint('home', __name__)
home_api = Api(home_bp)

api.add_resource(Demo, '/demo/')
api.add_resource(GetPlayer, '/getplayer/')

home_api.add_resource(Home, '/')
home_api.add_resource(PlayerData, '/player_data')
