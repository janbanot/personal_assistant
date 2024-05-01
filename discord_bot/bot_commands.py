from enum import Enum
from collections import namedtuple

Command = namedtuple("Command", ["name", "description"])


class BotCommands(Enum):
    LIST_COMMANDS = Command("list-commands", "List all available commands")
    YT_SUMMARY = Command(
        "yt-summary", "Get a summary of a YouTube video. Provide a URL"
    )
    CHECK_ENGLISH = Command(
        "check-english",
        "Check and fix grammatical, spelling, and punctuation errors in English text",
    )


def get_bot_commands():
    commands = []
    for command in BotCommands:
        commands.append(f"{command.value.name}: {command.value.description}")
    return "\n".join(commands)
