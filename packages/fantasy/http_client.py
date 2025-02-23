import logging
import sys
import time
import requests


class HTTPClient:
    def __init__(
        self, base_url: str, session: requests.Session, log_level: int
    ) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(log_level)
        self._logger.addHandler(logging.StreamHandler(sys.stdout))
        self._base_url = base_url
        self._session = session

    def get(self, path: str) -> requests.Response:
        self._logger.debug("Starting request for GET /{}".format(path))
        _start = time.time()
        _url = f"{self._base_url}/{path}"
        r = self._session.get(_url)
        self._logger.debug("Request execution took{}".format(time.time() - _start))
        r.raise_for_status()
        return r
