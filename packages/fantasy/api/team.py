from packages.fantasy.base_api import Base


class Team(Base):
    _endpoint = "entry"

    def get_id(self, team_id: str) -> dict:
        r = self._client.get(f"{self._endpoint}/{team_id}")
        return r.json()

    def get_transfers(self, team_id: str) -> dict:
        r = self._client.get(f"{self._endpoint}/{team_id}/transfers")
        return r.json()
