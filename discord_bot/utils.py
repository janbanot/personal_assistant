import requests
import json
import globals
from datetime import datetime, timedelta

URL = "http://assistant_proxy:8081/"


def is_token_valid():
    if (
        globals.api_token
        and globals.api_token_expires_at
        and globals.api_token_expires_at > datetime.now()
    ):
        return True
    else:
        login()
        if globals.api_token:
            return True
        else:
            return False


# TODO: change request to aiohttp
def login():
    url = URL + "login"
    headers = {"Content-Type": "application/json"}
    data = {"email": "test@test.com", "password": "test1"}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        globals.api_token = response_data.get("access_token")
        expires_in = response_data.get("expires_in")
        globals.api_token_expires_at = datetime.now() + timedelta(seconds=expires_in)
    else:
        globals.api_token = None
        globals.api_token_expires_at = None


def hello_world():
    auth_header = {"Authorization": f"Bearer {globals.api_token}"}
    response = requests.get(URL, headers=auth_header)
    return response.json()


def chat(message):
    headers = {
        "Authorization": f"Bearer {globals.api_token}",
        "Content-Type": "application/json"
    }
    url = URL + "chat"
    data = {"message": message}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()['message']


def clear_context():
    headers = {"Authorization": f"Bearer {globals.api_token}"}
    url = URL + "clear-context"
    response = requests.post(url, headers=headers)
    return response.json()['message']
