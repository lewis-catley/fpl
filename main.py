import os
import logging
import json

from packages.fantasy import AuthenticatedClient, Client

logging.basicConfig(level=logging.INFO)

_user_name = os.getenv("FPL_USERNAME")
_password = os.getenv("FPL_PASSWORD")

if _user_name and _password:
    _fpl_client = AuthenticatedClient(
        username=_user_name, password=_password, log_level=logging.INFO
    )
    # Lads, Lads, Lads ID: 820705
    _league = _fpl_client.league.get("820705")
    # print("{}".format(json.dumps(_league)))
    _lc_team_id = "3889417"
    _lc_team = _fpl_client.team.get_transfers(_lc_team_id)
    print("{}".format(json.dumps(_lc_team)))

else:
    _fpl_client = Client()
