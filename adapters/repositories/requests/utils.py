"""
Constants and auxiliary functions for the repositories
"""


from datetime import datetime


HF_API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b"
FOOTBALL_API_HOST_HEADER = "api-football-v1.p.rapidapi.com"
FOOTBALL_API_URL = f"https://{FOOTBALL_API_HOST_HEADER}/v3"

current_year: str = str(datetime.now().year)


def serverless_api_headers(api_token: str) -> dict[str, str]:
    """Create a header for a model request.

    Args:
        api_token (str): API Token to access a resource

    Returns:
        dict[str, str]: a headers dictionary for the request
    """
    return {"Authorization": f"Bearer {api_token}"}


def rapid_api_headers(
    key: str,
    host: str = FOOTBALL_API_HOST_HEADER,
) -> dict[str, str]:
    """Create a header for an Rapid API request.

    Args:
        key (str): API Token
        host (str): API host

    Returns:
        dict[str, str]: _description_
    """
    return {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": host,
    }
