import requests
import definitions

def get_pro_matches():
    requests_object = requests.get(definitions.PRO_MATCHES_REQUEST)
    requests_dictionary = requests_object.text
    print(requests_dictionary)

if __name__ == '__main__':
    get_pro_matches()
