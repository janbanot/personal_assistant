import os
import sys
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
from concurrent.futures import ThreadPoolExecutor
from utils import (
    login,
    is_token_valid,
    # hello_world,
    chat,
    # clear_context,
    yt_summary,
    page_summary,
    check_english,
    conversation_context_handler
)
from bot_commands import BotCommands, get_bot_commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN is not set")

GUILD_ID = os.getenv("DISCORD_GUILD_ID")
if not GUILD_ID:
    raise ValueError("DISCORD_GUILD_ID is not set")

MY_GUILD = discord.Object(id=GUILD_ID)

# chat, chat-testing
CHATTING_CHANNELS_IDS = [1238228569021349948, 1238223813997756446]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(sys.stdout)])


@bot.event
async def on_ready():
    login()
    print(f"{bot.user} has connected to Discord!")


@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    if message.channel.id in CHATTING_CHANNELS_IDS:
        await handle_bot_chatting(message)

    await bot.process_commands(message)


async def handle_bot_chatting(message):
    if is_token_valid():
        if message.content.startswith("!clear"):
            response = conversation_context_handler(force_clear=True)
        else:
            conversation_context_handler()
            response = chat(message.content)
        await message.channel.send(response)
    else:
        await message.channel.send("Could not get API token")


@bot.command(name="sync", description="Sync commands tree commands")
async def sync_command(ctx: commands.Context):
    bot.tree.copy_global_to(guild=MY_GUILD)
    await bot.tree.sync(guild=MY_GUILD)
    await ctx.send("Commands synced!")


# TODO: refactor to utilize async and remove duplicated code
# TODO: !!!! fix problem with unauthorized error on commands
# handle 401 errors + add handling for errors in api so in bot we can display anything
@bot.command(
    name=BotCommands.YT_SUMMARY.value.name,
    description=BotCommands.YT_SUMMARY.value.description,
)
async def yt_summary_command(ctx: commands.Context, url: str):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        summary = await loop.run_in_executor(pool, yt_summary, url)
    await ctx.send(summary)


@bot.command(
    name=BotCommands.PAGE_SUMMARY.value.name,
    description=BotCommands.PAGE_SUMMARY.value.description,
)
async def page_summary_command(ctx: commands.Context, url: str):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        summary = await loop.run_in_executor(pool, page_summary, url)
    await ctx.send(summary)


@bot.command(
    name=BotCommands.CHECK_ENGLISH.value.name,
    description=BotCommands.CHECK_ENGLISH.value.description,
)
async def check_english_command(ctx: commands.Context, *, input_text: str):
    fixed_text = check_english(input_text)
    await ctx.send(fixed_text)


@bot.tree.command(
    name=BotCommands.LIST_COMMANDS.value.name,
    description="Get a list of all available commands",
)
async def list_all_commands(interaction: discord.Interaction) -> None:
    commands_list = str(get_bot_commands())
    await interaction.response.send_message(commands_list)


bot.run(TOKEN)
