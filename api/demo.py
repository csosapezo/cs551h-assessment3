"""Demo endpoint"""


from flask_restful import Resource

from adapters.repositories.requests.football import FootballRepository
from adapters.repositories.requests.nlg import LanguageModelRepository


class Demo(Resource):
    """Demo"""
    def get(self):
        """Demo"""

        player_id = 109564
        fixture_id = "1094463"

        football_repo = FootballRepository()
        fixture: dict = football_repo.fixture_by_id(fixture_id)
        player_performance: dict = football_repo.player_performance(
            player_id,
            fixture_id,
        )

        llm_repo = LanguageModelRepository()
        output: str = llm_repo.generate_player_match_report(
            fixture,
            player_performance,
        )

        return {"response": output}, 200
