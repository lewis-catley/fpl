from packages.fantasy.base_api import Base

class League(Base):
    _endpoint = "leagues-classic"

    def get(self, id: str) -> dict:
        _url = f"{self._endpoint}/{id}"
        r = self._client.get(_url)
        return r.json()
