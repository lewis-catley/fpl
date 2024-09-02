import sys
import logging

from packages.fantasy.base_api import Base
from packages.fantasy.api.bootstrap import Bootstrap
from packages.fantasy.api.team import Team
from packages.fantasy.api.league import League

class Client():
    def __init__(self, log_level: int = logging.WARN, username: str | None = None, password: str | None = None) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(log_level)
        self._base_url = "https://fantasy.premierleague.com/api"

        self.bootstrap = Bootstrap(self._base_url, log_level, {})
        self.team = Team(self._base_url, log_level, {})
        self.league = League(self._base_url, log_level, {})
    
