import os
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

# TODO: refactor the file, because all theses will be simmilar, maybe there is a pattern for this
# TODO: change to use aiohttp instead of requests, so discord command can utilize async

load_dotenv()

EMAIL = os.getenv("API_USER_EMAIL")
PASSWORD = os.getenv("API_PASSWORD")
URL = os.getenv("API_URL")


def get_valid_token(config):
    if not config.is_token_valid():
        login()
    return config.is_token_valid()


def update_conversation_timestamp(config):
    config.current_conversation_last_message_timestamp = datetime.now()


def is_new_conversation(config):
    time_since_last_message = datetime.now() - config.current_conversation_last_message_timestamp
    return time_since_last_message > timedelta(minutes=10)


def conversation_context_handler(config, force_clear=False):
    if force_clear:
        config.current_conversation_id += 1
        update_conversation_timestamp()
        return clear_context()
    elif not config.current_conversation_id:
        config.current_conversation_id = 1
        update_conversation_timestamp()
    elif is_new_conversation():
        config.current_conversation_id += 1
        update_conversation_timestamp()
        clear_context()
    else:
        update_conversation_timestamp()

    return None


# TODO: change request to aiohttp
def login(config):
    url = URL + "login"
    headers = {"Content-Type": "application/json"}
    data = {"email": EMAIL, "password": PASSWORD}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        config.api_token = response_data.get("access_token")
        expires_in = response_data.get("expires_in")
        config.api_token_expires_at = datetime.now() + timedelta(seconds=expires_in)
    else:
        config.api_token = None
        config.api_token_expires_at = None


def hello_world(config):
    auth_header = {"Authorization": f"Bearer {config.api_token}"}
    response = requests.get(URL, headers=auth_header)
    return response.json()


def chat(config, message):
    headers = {
        "Authorization": f"Bearer {config.api_token}",
        "Content-Type": "application/json",
    }
    url = URL + "chat"
    data = {"message": message}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["message"]


# TODO: refactor to get rid of duplicated code
def clear_context(config):
    headers = {"Authorization": f"Bearer {config.api_token}"}
    url = URL + "clear-context"
    response = requests.post(url, headers=headers)
    return response.json()["message"]


def yt_summary(config, video_url):
    headers = {
        "Authorization": f"Bearer {config.api_token}",
        "Content-Type": "application/json",
    }
    url = URL + "yt-summary"
    data = {"url": video_url}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["summary"]


def page_summary(config, page_url):
    headers = {
        "Authorization": f"Bearer {config.api_token}",
        "Content-Type": "application/json",
    }
    url = URL + "page-summary"
    data = {"url": page_url}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["summary"]


def check_english(config, text):
    headers = {
        "Authorization": f"Bearer {config.api_token}",
        "Content-Type": "application/json",
    }
    url = URL + "check-english"
    data = {"text": text}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["text"]
