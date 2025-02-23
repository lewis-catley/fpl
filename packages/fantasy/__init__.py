import logging
import requests

from packages.fantasy.base_api import Base
from packages.fantasy.exceptions import FPLUnauthenticatedException
from packages.fantasy.api.bootstrap import Bootstrap
from packages.fantasy.api.team import Team
from packages.fantasy.api.league import League


class Client:
    def __init__(
        self,
        log_level: int = logging.WARN,
    ) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(log_level)
        self._base_url = "https://fantasy.premierleague.com/api"

        self._session = requests.Session()

        self.__base = Base(self._base_url, self._session, log_level)

        self.bootstrap = Bootstrap(self._base_url, self._session, log_level)


class AuthenticatedClient(Client):
    def __init__(
        self, username: str, password: str, log_level: int = logging.WARN
    ) -> None:
        super().__init__(log_level)

        self.__authenticate(username, password)

        self.team = Team(self._base_url, self._session, log_level)
        self.league = League(self._base_url, self._session, log_level)

    def __authenticate(self, username: str, password: str) -> None:
        """Authentication logic for the FPL API."""
        __login_url = "https://users.premierleague.com/accounts/login/"
        __payload = {
            "login": username,
            "password": password,
            "app": "plfpl-web",
            "redirect_uri": "https://fantasy.premierleague.com/",
        }
        # TODO: This was just lifted from the debug network tab
        # I'm sure all of these aren't required.
        _cloned_headers = [
            {
                "name": "Accept",
                "value": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            },
            {"name": "Accept-Encoding", "value": "gzip, deflate, br, zstd"},
            {"name": "Accept-Language", "value": "en-US,en;q=0.5"},
            {"name": "Connection", "value": "keep-alive"},
            {"name": "Content-Length", "value": "134"},
            {"name": "Content-Type", "value": "application/x-www-form-urlencoded"},
            {"name": "Origin", "value": "null"},
            {"name": "Priority", "value": "u=0, i"},
            {"name": "Sec-Fetch-Dest", "value": "document"},
            {"name": "Sec-Fetch-Mode", "value": "navigate"},
            {"name": "Sec-Fetch-Site", "value": "same-site"},
            {"name": "Sec-Fetch-User", "value": "?1"},
            {"name": "TE", "value": "trailers"},
            {"name": "Upgrade-Insecure-Requests", "value": "1"},
            {
                "name": "User-Agent",
                "value": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
            },
        ]

        __headers = {}
        for h in _cloned_headers:
            __headers[h["name"]] = h["value"]

        with self._session.post(
            url=__login_url, data=__payload, headers=__headers, allow_redirects=True
        ) as response:
            if response.status_code == 403:
                self._logger.error(
                    "403 forbidden, unable to authenticate with FPL API, %s",
                    response.content,
                )
                raise FPLUnauthenticatedException()
            self._logger.debug("Authentication response: %s", response.status_code)
