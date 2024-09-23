import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("Bot is ready!")
    print("--------------")

async def main():
    try:
        print("Attempting to load cogs...")
        await client.load_extension('cogs.music')
    except Exception as e:
        print(f"Error loading cogs: {e}")

    bot_token = os.getenv('DISCORD_BOT_TOKEN')
    print("Starting bot...")
    await client.start(bot_token)

asyncio.run(main())
