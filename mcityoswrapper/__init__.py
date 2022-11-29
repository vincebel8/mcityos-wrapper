#__init__.py

import os
import requests

OCTANE_API_KEY = "reticulatingsplines"

class APIKeyMissingError(Exception):
        pass

if OCTANE_API_KEY is None:
        raise APIKeyMissingError("Need API key")

session = requests.Session()
session.params = {}
session.headers = {
    'accept': 'application/json',
    'X-API-KEY': OCTANE_API_KEY,
    'Content-Type': 'application/json',
}

from .mcityos_intersections import McityOSIntersections
from .mcityos_rail import McityOSRail
