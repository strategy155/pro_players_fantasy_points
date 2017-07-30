import requests
import definitions
import json
import time


def get_ti_teams(teams_request):
    ti_teams = []
    for team in teams_request:
        if team['name'] in definitions.TEAM_NAME_LIST:
            ti_teams.append(team)
    return ti_teams


def get_pro_players_to_tag(pro_players_request):
    ti_players = {}
    for player in pro_players_request:
        team_tag = player['team_tag']
        if team_tag:
            team_tag_lowered = team_tag.lower()
            is_locked = player['is_locked']
            name = player['name']
            if (team_tag_lowered in definitions.TEAM_TAG_LIST):
                if team_tag_lowered == 'xctn' and name in definitions.XCTN_TEAM:
                    ti_players.setdefault(team_tag, []).append(player)
                elif team_tag_lowered != 'xctn' and is_locked:
                    ti_players.setdefault(team_tag, []).append(player)
    return ti_players


def get_real_time(epoch_time_string):
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time_string))
    return time_str


def get_request(api_method, params={}):
    requests_object = requests.get(api_method, params=params)
    requests_dictionary_text = requests_object.text
    requests_dictionary_unjsoned = json.loads(requests_dictionary_text)
    return requests_dictionary_unjsoned


def get_all_pro_matches():
    params = {}
    while True:
        pro_matches_request = get_request(definitions.PRO_MATCHES_REQUEST, params=params)
        time.sleep(1)
        last_match = pro_matches_request[-1]
        print(last_match['match_id'], params)
        params['less_than_match_id'] = last_match['match_id']


def parse_pro_matches_request(pro_matches_request):
    for match in pro_matches_request:
        print(match['dire_name'], match['radiant_name'])




if __name__ == '__main__':
    # pro_players_request = get_request(definitions.PRO_PLAYERS_REQUEST)
    # ti_players = get_pro_players_to_tag(pro_players_request)
    # pro_matches_request = get_request(definitions.PRO_MATCHES_REQUEST)
    # parse_pro_matches_request(pro_matches_request)
    teams_request = get_request(definitions.TEAMS_REQUEST)
    ti_teams = get_ti_teams(teams_request)


