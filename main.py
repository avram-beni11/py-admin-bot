import os, datetime, discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Logged in!")

# @bot.tree.command(name="testing") #Name of the / command
# async def test(i: discord.Interaction, member: discord.Member): #Define action. discord interaction, specify member
#     await i.response.send_message("Hello!") #Once done, reply with message

@bot.tree.command(
        name="mute",
        description="Mute a member for X amount of minues"
                  )
@app_commands.default_permissions(moderate_members=True)
async def mute(i: discord.Interaction, member: discord.Member, minutes: int , reason: str):
    await member.timeout(datetime.timedelta(minutes=minutes))
    await i.response.send_message(f"{member} was muted for {minutes} minutes")

bot.run(os.getenv("DISCORD_TOKEN"))