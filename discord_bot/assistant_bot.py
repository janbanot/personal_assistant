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
    hello_world,
    chat,
    clear_context,
    yt_summary,
    page_summary,
    check_english,
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
    if message.author == bot.user:
        return

    # TODO: figure out a better way to handle this
    if message.content.startswith("$hello"):
        if is_token_valid():
            await message.channel.send("Hello!")
            await message.channel.send(hello_world())
        else:
            await message.channel.send("Could not get API token")

    if message.content.startswith("$q"):
        if is_token_valid():
            await message.channel.send(chat(message.content[3:]))
        else:
            await message.channel.send("Could not get API token")

    if message.content.startswith("$clear"):
        if is_token_valid():
            await message.channel.send(clear_context())
        else:
            await message.channel.send("Could not get API token")
    # added to process commands, otherwise the bot will not respond to commands
    await bot.process_commands(message)


@bot.command(name="sync", description="Sync commands tree commands")
async def sync_command(ctx: commands.Context):
    bot.tree.copy_global_to(guild=MY_GUILD)
    await bot.tree.sync(guild=MY_GUILD)
    await ctx.send("Commands synced!")


# TODO: refactor to utilize async and remove duplicated code
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
