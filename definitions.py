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
TEAM_TAG_LIST = [
    "og",
    "vp",
    "eg",
    "liquid",
    "ig",
    "newbee",
    "secret",
    "hr",
    "empire",
    "ig.v",
    'lfy',
    'lgd',
    'tnc',
    'fnatic',
    "c9",
    "dc",
    "infamous",
    "xctn"
]
TEAM_NAME_LIST = [
    "Team Liquid",
    "Virtus.pro",
    "Evil Geniuses",
    "LGD.Forever Young",
    "LGD-GAMING",
    "Newbee",
    "TNC Pro Team",
    "Team Secret",
    "OG Dota2",
    "Invictus Gaming",
    "Team Empire",
    "Fnatic",
    "Digital Chaos",
    "iG.Vitality",
    "Execration",
    "Infamous、",
    "Cloud9",
    "HellRaisers"
]
XCTN_TEAM= [
    "LeumiK",
    "James",
    "Nando",
    "Raging Potato",
    "Rr~"
]