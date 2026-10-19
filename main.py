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
async def mute(i: discord.Interaction, member: discord.Member, minutes: int , reason: str="No reason fiven"):
    await member.timeout(datetime.timedelta(minutes=minutes))
    await i.response.send_message(f"{member} was muted for {minutes} minutes")

@bot.tree.command(
        name="kick",
        description="Kick a member"
                  )
@app_commands.default_permissions(kick_members=True)
async def kick(i: discord.Interaction, member: discord.Member, reason: str="no reason given"):
    await member.kick()
    await i.response.send_message(f"{member} was kicked for {reason}")

@bot.tree.command(
        name="ban",
        description="Ban a member"
                  )
@app_commands.default_permissions(ban_members=True)
async def ban(i: discord.Interaction, member: discord.Member, reason: str="no reason given"):
    await member.ban()
    await i.response.send_message(f"{member} was banned for {reason}")

bot.run(os.getenv("DISCORD_TOKEN"))