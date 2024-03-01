"""Home"""


from flask import current_app
from flask_restful import Resource


class Home(Resource):
    """Demo"""
    def get(self):
        return current_app.send_static_file('index.html')


class PlayerData(Resource):
    """Demo"""
    def get(self):
        return current_app.send_static_file('player_data.json')
