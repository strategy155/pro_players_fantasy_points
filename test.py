import requests
import definitions
import json

def get_pro_matches():
    requests_object = requests.get(definitions.TEAMS_METHOD)
    requests_dictionary_text = requests_object.text
    requests_dictionary_unjsoned = json.loads(requests_dictionary_text)
    print(requests_dictionary_unjsoned[0])

if __name__ == '__main__':
    get_pro_matches()
