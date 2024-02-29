"""
Gemma-7B model repository to get responses from its serverless API
"""

import json

from attrs import define
from dotenv import dotenv_values
import requests

from adapters.repositories.requests.utils import (
    HF_API_URL as API_URL,
    serverless_api_headers as headers,
)


@define
class LanguageModelRepository:
    """Repository to make requests to Gemma-7B"""

    api_token: str = dotenv_values(".env")["API_TOKEN"]

    def generic_query_model(self, query: str) -> str:
        """Get and answer from the Language Model Repository"""
        response: requests.Response = requests.post(
            API_URL,
            headers=headers(api_token=self.api_token),
            json={"inputs": query},
            timeout=600,
        )

        return response.json()[0]["generated_text"]

    def generate_player_match_report(
        self,
        fixture_data: dict,
        player_data: dict,
    ) -> str:

        """Generate a tailored game report for a specific player"""

        home_team = fixture_data["teams"]["home"]["name"]
        away_team = fixture_data["teams"]["away"]["name"]

        player_name = player_data["player"]["player"]["name"]
        player_team = player_data["team"]["name"]
        opponent_team = away_team if player_team == home_team else home_team

        prompt = f"""
        Considering the following match data for the game between {home_team} and {away_team}
        {json.dumps(fixture_data)}

        and the stastistics from {player_team}'s player {player_name} for the previously mentioned match
        {json.dumps(player_data)}

        A possible in-depth performance analysis for {player_name} that takes into consideration his impact in the game would be the following:

        {player_name} performance in the game against {opponent_team} was
        """

        raw_response: str = self.generic_query_model(prompt)

        aux_line = "would be the following:"
        last_sentence_index: int = raw_response.rfind(".")
        response_index: int = raw_response.find(aux_line) + len(aux_line)
        response: str = raw_response[response_index:last_sentence_index + 1]

        return " ".join(response.split())
