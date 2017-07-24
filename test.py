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
            if team_tag_lowered in definitions.TEAM_LIST and is_locked:
                ti_players.setdefault(team_tag, []).append(player)
    for team in ti_players.keys():
        print(team, end=':\t')
        for player in ti_players[team]:
            print(player, end='\t')
        print(len(ti_players[team]))


if __name__ == '__main__':
    pro_players_request = get_pro_players_request()
    get_pro_players_to_tag(pro_players_request)
