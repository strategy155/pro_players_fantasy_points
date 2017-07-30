import requests
import definitions
import json
import time

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


def get_real_time(epoch_time_string):
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time_string))
    return time_str


def get_request(api_method):
    requests_object = requests.get(api_method)
    requests_dictionary_text = requests_object.text
    requests_dictionary_unjsoned = json.loads(requests_dictionary_text)
    return requests_dictionary_unjsoned


if __name__ == '__main__':
    pro_players_request = get_request(definitions.PRO_PLAYERS_REQUEST)
    pro_matches_request = get_request(definitions.PRO_MATCHES_REQUEST)
    ti_players = get_pro_players_to_tag(pro_players_request)
    print(get_real_time(pro_matches_request[-1]['start_time']))
