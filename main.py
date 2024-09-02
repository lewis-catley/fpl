import os
import logging
import json

from packages.fantasy import Client

_user_name = os.getenv("FPL_USERNAME")
_password = os.getenv("PASSWORD")

_fpl_client = Client(logging.INFO)

# LC Team ID: 3889417
_lc_team_id = "3889417"
_lc_team = _fpl_client.team.get_id(_lc_team_id)


# Lads, Lads, Lads ID: 820705
_league = _fpl_client.league.get("820705")

print("{}".format(json.dumps(_league)))
