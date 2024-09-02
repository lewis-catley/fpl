from packages.fantasy.base_api import Base

class Team(Base):
    _endpoint = "entry"

    def get_id(self, id: str) -> dict:
        r = self._client.get(f"{self._endpoint}/{id}")
        return r.json()
