from enum import Enum
from collections import namedtuple

Command = namedtuple("Command", ["name", "description"])


class BotCommands(Enum):
    LIST_COMMANDS = Command("list-commands", "list all available commands")
    YT_SUMMARY = Command(
        "yt-summary", "get a summary of a YouTube video, provide a URL"
    )
    PAGE_SUMMARY = Command(
        "page-summary", "get a summary of a page, provide a URL"
    )
    CHECK_ENGLISH = Command(
        "check-english",
        "check and fix grammatical, spelling, and punctuation errors in English text",
    )


def get_bot_commands():
    commands = []
    for command in BotCommands:
        commands.append(f"- **{command.value.name}**: {command.value.description}")
    return "\n".join(commands)
