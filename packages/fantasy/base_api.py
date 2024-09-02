import logging
import requests

from packages.fantasy.http_client import HTTPClient

class Base():
    """Base class that all endpoints inherit"""
    def __init__(self, base_url: str, log_level: int, headers: dict) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(log_level)

        self._client = HTTPClient(base_url, log_level, headers)
