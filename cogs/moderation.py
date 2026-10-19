import os, datetime, discord
from discord import app_commands
from discord.ext import commands

@bot.tree.command(name="mute")
@app_commands.default_permissions(mute_members=True)
async def mute(i: discord.Interaction, member: discord.Member ):
    await i.response.send_message("{member} was muted")