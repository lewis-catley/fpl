from typing import Literal


class League:
    id: int
    name: str
    bans: list
    created: str
    has_cup: bool
    closed: bool
    privacy: Literal["p"]
