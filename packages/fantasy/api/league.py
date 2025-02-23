from packages.fantasy.base_api import Base


class League(Base):
    _endpoint = "leagues-classic"

    def get(self, league_id: str) -> dict:
        _url = f"{self._endpoint}/{league_id}"
        r = self._client.get(_url)
        return r.json()

    def standings(self, league_id: str) -> dict:
        _url = f"{self._endpoint}/{league_id}/standings"
        r = self._client.get(_url)
        return r.json()
