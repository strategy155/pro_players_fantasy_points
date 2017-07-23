import requests
import definitions
import json

def get_pro_players_request():
    requests_object = requests.get(definitions.PRO_PLAYERS_REQUEST)
    requests_dictionary_text = requests_object.text
    requests_dictionary_unjsoned = json.loads(requests_dictionary_text)
    return requests_dictionary_unjsoned


def get_pro_players_to_tag(pro_players_request):
    print('')
    for player in pro_players_request:
        name = player['name']
        team_tag = player['team_tag']
        team_tag_lowered = team_tag.lower()
        is_locked = player['is_locked']
        if team_tag_lowered in definitions.TEAM_LIST and is_locked:
            print(name, team_tag, end='\t')


def get_players_of_ti7(pro_players):



if __name__ == '__main__':
    pro_players_request = get_pro_players_request()
    get_pro_players_to_tag(pro_players_request)
