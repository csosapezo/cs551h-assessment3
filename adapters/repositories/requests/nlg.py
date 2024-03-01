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

    def player_team_result_verb(
        self,
        home_team: str,
        home_won: bool,
        away_won: bool,
        player_team: str,
    ):
        if player_team == home_team:
            if home_won:
                return "victory"
            if away_won:
                return "loss"
        else:
            if home_won:
                return "loss"
            if away_won:
                return "victory"
        
        return "draw"

    def generate_player_match_report(
        self,
        fixture_data: dict,
        player_data: dict,
    ) -> str:

        """Generate a tailored game report for a specific player"""

        home_team = fixture_data["teams"]["home"]["name"]
        home_team_won = fixture_data["teams"]["home"]["winner"]

        away_team = fixture_data["teams"]["away"]["name"]
        away_team_won = fixture_data["teams"]["away"]["winner"]

        player_name = player_data["player"]["player"]["name"]
        player_team = player_data["team"]["name"]
        opponent_team = away_team if player_team == home_team else home_team

        result_verb = self.player_team_result_verb(
            home_team,
            home_team_won,
            away_team_won,
            player_team,
        )

        prompt = f"""
        User:
        You are a football data analyst who was asked to write a report of a player performance after a match.

        Considering the following match data for the game between {home_team} and {away_team}
        {json.dumps(fixture_data)}

        and the stastistics from {player_team}'s player {player_name} for the previously mentioned match
        {json.dumps(player_data)}

        Write an in-depth performance analysis for {player_name} that takes into consideration his impact in the game.
        If {player_team}'s won, highlight his main abilities and how they were influential for their victory.
        If his team lost, explain how {player_name} was responsible of their bad result in that specific game.

        Model:
        {player_name} performance in the {player_team} {result_verb} against {opponent_team} was
        """

        raw_response: str = self.generic_query_model(prompt)

        aux_line = "Model:"
        response_index: int = raw_response.find(aux_line) + len(aux_line)
        response: str = raw_response[response_index:]

        return " ".join(response.split())
