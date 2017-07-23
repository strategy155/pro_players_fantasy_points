import urllib

BASE_API_SERVER = "https://api.opendota.com/api/"
PRO_MATCHES_METHOD = "proMatches"
MATCHES_METHOD = "matches"
PLAYERS_METHOD = "players"
TEAMS_METHOD = "teams"
PRO_PLAYERS_METHOD = "proPlayers"
PRO_MATCHES_REQUEST = urllib.parse.urljoin(BASE_API_SERVER, PRO_MATCHES_METHOD)
MATCHES_REQUEST = urllib.parse.urljoin(BASE_API_SERVER, MATCHES_METHOD)
TEAMS_REQUEST = urllib.parse.urljoin(BASE_API_SERVER, TEAMS_METHOD)
PRO_PLAYERS_REQUEST = urllib.parse.urljoin(BASE_API_SERVER, PRO_PLAYERS_METHOD)
TEAM_LIST = [
    "OG",
    "VP",
    "EG",
    "Liquid",
    "IG",
    "Newbee",
    "Secret",
    "HR",
    "Empire",
    "iG.V",
    'LFY',
    'LGD',
    'TNC',
    'Fnatic',
    'Execration',
    "C9",
    "DC",
    "Infamous"
]