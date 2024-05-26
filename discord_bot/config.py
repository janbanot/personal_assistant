import os
from datetime import datetime


class Config:
    def __init__(self):
        self._api_token = None
        self._api_token_expires_at = None
        self._current_conversation_id = None
        self._current_conversation_last_message_timestamp = None
        self.discord_token = os.getenv("DISCORD_TOKEN")
        self.discord_guild_id = os.getenv("DISCORD_GUILD_ID")
        # chat, chat-testing
        self.chatting_channels_ids = [1238228569021349948, 1238223813997756446]

        if not self.discord_token:
            raise ValueError("DISCORD_TOKEN is not set")

        if not self.discord_guild_id:
            raise ValueError("DISCORD_GUILD_ID is not set")

    @property
    def api_token(self):
        return self._api_token

    @api_token.setter
    def api_token(self, value):
        self._api_token = value

    @property
    def api_token_expires_at(self):
        return self._api_token_expires_at

    @api_token_expires_at.setter
    def api_token_expires_at(self, value):
        self._api_token_expires_at = value

    def is_token_valid(self):
        return (
            self.api_token
            and self.api_token_expires_at
            and self.api_token_expires_at > datetime.now()
        )

    @property
    def current_conversation_id(self):
        return self._current_conversation_id

    @current_conversation_id.setter
    def current_conversation_id(self, value):
        self._current_conversation_id = value

    @property
    def current_conversation_last_message_timestamp(self):
        return self._current_conversation_last_message_timestamp

    @current_conversation_last_message_timestamp.setter
    def current_conversation_last_message_timestamp(self, value):
        self._current_conversation_last_message_timestamp = value