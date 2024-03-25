import os
import sys
import logging
import discord
from dotenv import load_dotenv
from utils import login, is_token_valid, hello_world, chat, clear_context

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(sys.stdout)])


@client.event
async def on_ready():
    login()
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

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


client.run(TOKEN)
