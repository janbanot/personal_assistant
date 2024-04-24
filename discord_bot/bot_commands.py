from enum import Enum


class BotCommands(Enum):
    LIST_COMMANDS = "list-commands"
    SYNC = "sync"
    YT_SUMMARY = "yt-summary"


def get_bot_commands():
    for command in BotCommands:
        return [command.value for command in BotCommands]
