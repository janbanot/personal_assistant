import os
import requests
import json
import globals
from datetime import datetime, timedelta
from dotenv import load_dotenv

# TODO: refactor the file, because all theses will be simmilar, maybe there is a pattern for this
# TODO: change to use aiohttp instead of requests, so discord command can utilize async

load_dotenv()

EMAIL = os.getenv("API_USER_EMAIL")
PASSWORD = os.getenv("API_PASSWORD")
URL = os.getenv("API_URL")


def is_token_valid():
    if (
        # TODO: change to use something else instead of globals to store the token and expiration
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
    data = {"email": EMAIL, "password": PASSWORD}
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
        "Content-Type": "application/json",
    }
    url = URL + "chat"
    data = {"message": message}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["message"]


# TODO: refactor to get rid of duplicated code
def clear_context():
    headers = {"Authorization": f"Bearer {globals.api_token}"}
    url = URL + "clear-context"
    response = requests.post(url, headers=headers)
    return response.json()["message"]


def yt_summary(video_url):
    headers = {
        "Authorization": f"Bearer {globals.api_token}",
        "Content-Type": "application/json",
    }
    url = URL + "yt-summary"
    data = {"url": video_url}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["summary"]


def page_summary(page_url):
    headers = {
        "Authorization": f"Bearer {globals.api_token}",
        "Content-Type": "application/json",
    }
    url = URL + "page-summary"
    data = {"url": page_url}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["summary"]


def check_english(text):
    headers = {
        "Authorization": f"Bearer {globals.api_token}",
        "Content-Type": "application/json",
    }
    url = URL + "check-english"
    data = {"text": text}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["text"]
