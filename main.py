import os, datetime, discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members = True

class Bot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.moderation")
        await self.tree.sync()

bot = Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot online") 

bot.run(os.getenv("DISCORD_TOKEN"))