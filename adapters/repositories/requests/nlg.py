"""
Gemma-7B model repository to get responses from its serverless API
"""

from attrs import define
from dotenv import dotenv_values
import requests

from adapters.repositories.requests.utils import API_URL, headers


@define
class LanguageModelRepository:
    """Repository to make requests to Gemma-7B"""

    api_token: str = dotenv_values(".env")["API_TOKEN"]

    def generic_query_model(self, query: str) -> str:
        """Get and answer from the Language Model Repository"""
        response: requests.Response = requests.post(
            API_URL,
            headers=headers(self.api_token),
            json={"inputs": query},
            timeout=600,
        )

        return response.json()[0]["generated_text"]
