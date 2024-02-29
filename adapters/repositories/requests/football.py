"""
Football repository to get responses from Rapid API
"""

from attrs import define
from dotenv import dotenv_values
import requests

from adapters.repositories.requests.utils import (
    FOOTBALL_API_URL as API_URL,
    rapid_api_headers as headers,
    current_year,
)


@define
class FootballRepository:
    """Repository to make requests to the football API"""

    api_key: str = dotenv_values(".env")["RAPID_API_KEY"]

    def generic_api_request(self, params: dict, endpoint: str) -> dict:
        """Get and answer from Rapid API"""

        response: requests.Response = requests.get(
            f"{API_URL}/{endpoint}",
            headers=headers(self.api_key),
            params=params,
            timeout=600,
        )

        response_dict: dict = response.json()

        return response_dict["response"]

    def team_fixtures(self, team_id: str, season: str = current_year) -> dict:
        """Get matches for a team in a specific season"""
        params: dict = {
            "season": season,
            "team": team_id,
        }

        return self.generic_api_request(
            endpoint="fixtures",
            params=params,
        )

    def fixture_by_id(self, fixture_id: str) -> dict:
        """Get match by id"""
        params: dict = {
            "id": fixture_id,
        }

        raw_response: dict = self.generic_api_request(
            endpoint="fixtures",
            params=params,
        )[0]

        response = {
            "league": raw_response["league"],
            "teams": raw_response["teams"],
            "goals": raw_response["goals"],
        }

        return response

    def player_performance(
        self,
        player_id: int,
        fixture_id: str,
        is_away: bool = False,
    ) -> dict:
        """Get player performance"""
        params: dict = {"fixture": fixture_id}

        response: dict = self.generic_api_request(
            endpoint="fixtures/players",
            params=params,
        )

        team_index: int = 1 if is_away else 0

        for player in response[team_index]["players"]:

            if player["player"]["id"] == player_id:
                return {
                    "team": response[team_index]["team"],
                    "player": player,
                }

        raise ValueError
