"""
Gemma-7B model repository to get responses from any source
"""

from attrs import define


@define
class LanguageModelRepository:
    """Repository to make requests to Gemma-7B"""

    def generate_player_match_report(self, player_data: dict) -> str:
        """Generate a tailored game report for a specific player"""
        raise NotImplementedError
