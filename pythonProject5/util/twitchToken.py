import requests
import json

conf_file = open("../conf/config.json")
conf = json.load(conf_file)

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {"client_id":conf["clientId"],"client_secret":conf["clientSecret"],"grant_type":"client_credentials"}
auth_token = None

def setup_token():
    global auth_token
    r = requests.post("https://id.twitch.tv/oauth2/token", data=data, headers=headers)
    auth_token = r.json()
    return auth_token


if __name__ == "__main__":
    print(r)
    print(auth_token)
