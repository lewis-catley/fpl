from packages.fantasy.base_api import Base

class Bootstrap(Base):
    _endpoint = "bootstrap-static"

    def get(self) -> dict:
        r = self._client.get(self._endpoint)
        return r.json()

