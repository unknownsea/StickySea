import discord
from discord.ext import commands
import os
from config import PREFIX, TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

COGS = ["stickies"]

async def load_extensions():
    for cog in COGS:
        await bot.load_extension(f"cogs.{cog}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

import asyncio
asyncio.run(main())