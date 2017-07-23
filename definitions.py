import urllib

BASE_API_SERVER = "https://api.opendota.com/api/"
PRO_MATCHES_METHOD = "proMatches"
MATCHES_METHOD = "matches"
PLAYERS_METHOD = "players"
TEAMS_METHOD = "teams"
PRO_MATCHES_REQUEST = urllib.parse.urljoin(BASE_API_SERVER, PRO_MATCHES_METHOD)
MATCHES_REQUEST = urllib.parse.urljoin(BASE_API_SERVER, MATCHES_METHOD)
TEAMS_REQUEST = urllib.parse.urljoin(BASE_API_SERVER, TEAMS_METHOD)
