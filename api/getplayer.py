from flask_restful import Resource, reqparse

from adapters.repositories.requests.football import FootballRepository
from adapters.repositories.requests.nlg import LanguageModelRepository

class GetPlayer(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('player_id', type=int, required=True, help='No player_id provided', location='args')
        self.reqparse.add_argument('fixture_id', type=str, required=True, help='No fixture_id provided', location='args')
        super(GetPlayer, self).__init__()

    def get(self):

        args = self.reqparse.parse_args()
        player_id = args['player_id']
        fixture_id = args['fixture_id']

        football_repo = FootballRepository()
        fixture: dict = football_repo.fixture_by_id(fixture_id)
        player_performance: dict = football_repo.player_performance(player_id, fixture_id)

        llm_repo = LanguageModelRepository()
        output: str = llm_repo.generate_player_match_report(fixture, player_performance)

        return {"response": output}, 200
