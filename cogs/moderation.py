import os, datetime, discord
from discord import app_commands
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        #Mute user
        @bot.tree.command(
                name="mute",
                description="Mute a member for X amount of minues"
                        )
        @app_commands.default_permissions(moderate_members=True)
        async def mute(i: discord.Interaction, member: discord.Member, minutes: int , reason: str=" "):
            await member.timeout(datetime.timedelta(minutes=minutes))
            await i.response.send_message(f"{member} was muted for {minutes} minutes | {reason}")

        #Kick user
        @bot.tree.command(
                name="kick",
                description="Kick a member"
                        )
        @app_commands.default_permissions(kick_members=True)
        async def kick(i: discord.Interaction, member: discord.Member, reason: str=" "):
            await member.kick()
            await i.response.send_message(f"{member} was kicked | {reason}")

        #Ban user command
        @bot.tree.command(
                name="ban",
                description="Ban a member"
                        )
        @app_commands.default_permissions(ban_members=True)
        async def ban(i: discord.Interaction, member: discord.Member, reason: str=" "):
            await member.ban()
            await i.response.send_message(f"{member} was banned | {reason}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))