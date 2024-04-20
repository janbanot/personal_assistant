import os
import sys
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils import login, is_token_valid, hello_world, chat, clear_context

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("DISCORD_GUILD_ID")
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


@bot.command(name="sync")
async def sync_command(ctx):
    bot.tree.copy_global_to(guild=MY_GUILD)
    await bot.tree.sync(guild=MY_GUILD)
    await ctx.send("Commands synced!")


@bot.tree.command(name="command-1")
async def my_command_1(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Hello from command 1!")

bot.run(TOKEN)
