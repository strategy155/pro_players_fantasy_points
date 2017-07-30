import requests
import definitions
import json

def get_pro_players_request():
    requests_object = requests.get(definitions.PRO_PLAYERS_REQUEST)
    requests_dictionary_text = requests_object.text
    requests_dictionary_unjsoned = json.loads(requests_dictionary_text)
    return requests_dictionary_unjsoned


def get_pro_players_to_tag(pro_players_request):
    ti_players = {}
    for player in pro_players_request:
        team_tag = player['team_tag']
        if team_tag:
            team_tag_lowered = team_tag.lower()
            is_locked = player['is_locked']
            name = player['name']
            if (team_tag_lowered in definitions.TEAM_LIST and is_locked) or (team_tag_lowered == 'xctn' and name in definitions.XCTN_TEAM):
                ti_players.setdefault(team_tag, []).append(player)
    return ti_players

if __name__ == '__main__':
    pro_players_request = get_pro_players_request()
    get_pro_players_to_tag(pro_players_request)
