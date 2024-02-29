"""
Football repository to get responses from any source
"""

from attrs import define


@define
class FootballRepository:
    """Repository to make requests to the football API"""

    def team_fixtures(self, team_id: str, season: str) -> dict:
        """Get matches for a team in a specific season"""
        raise NotImplementedError

    def player_performance(
        self,
        player_id: str,
        fixture_id: str,
        is_away: bool = False,
    ) -> dict:
        """Get player performance"""
        raise NotImplementedError
