import logging
import sys
import time
import requests

class HTTPClient():
    def __init__(self, base_url: str, log_level: int, headers: dict) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(log_level)
        self._logger.addHandler(logging.StreamHandler(sys.stdout))
        self._base_url = base_url

    def get(self, path: str) -> None:
        _start = time.time()
        self._logger.debug("Starting request for GET /{}".format(path))
        _url = f"{self._base_url}/{path}"
        r = requests.get(_url)
        self._logger.debug("Reequest execution took{}".format(time.time() - _start))
        r.raise_for_status()
        return r
