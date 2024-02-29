"""
Constants and auxiliary functions for the repositories
"""


API_URL = "https://api-inference.huggingface.co/models/google/gemma-7b"


def headers(api_token: str) -> dict[str, str]:
    """Create a header for a model request.

    Args:
        api_token (str): API Token to access a resource

    Returns:
        dict[str, str]: a headers dictionary for the request
    """
    return {"Authorization": f"Bearer {api_token}"}
