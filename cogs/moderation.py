import datetime, discord
from discord import app_commands
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
        #Mute user
        @bot.tree.command(name="mute", description="Mute a member so they cannot type")
        @app_commands.default_permissions(moderate_members=True)
        async def mute(i: discord.Interaction, member: discord.Member, duration: int , reason: str="No reason provided"):
            await member.timeout(datetime.timedelta(duration),reason=reason)
            embed = discord.Embed(title="🔇User Muted", description=(
                                f"**Member:** {member.mention} \n"
                                f"**Duration:** {duration} minutes \n"
                                f"**Reason:** {reason}" ),
                                color=discord.Color.blurple())
            embed.set_footer(text="Moderation • Timeout")
            await i.response.send_message(embed=embed)

        #Kick user
        @bot.tree.command(name="kick",description="Kick a member")
        @app_commands.default_permissions(kick_members=True)
        async def kick(i: discord.Interaction, member: discord.Member, reason: str="No reason provided"):
            await member.kick()
            embed = discord.Embed(title="👢User Kicked", description=(
                                            f"**Member:** {member.mention} \n"
                                            f"**Reason:** {reason}" ),
                                            color=discord.Color.blurple())
            embed.set_footer(text="Moderation • Kick")
            await i.response.send_message(embed=embed)
            

        #Ban user command
        @bot.tree.command(name="ban",description="Ban a member")
        @app_commands.default_permissions(ban_members=True)
        async def ban(i: discord.Interaction, member: discord.Member, reason: str="No reason provided"):
            await member.ban()
            embed = discord.Embed(title="🔨User Banned", description=(
                                            f"**Member:** {member.mention} \n"
                                            f"**Reason:** {reason}" ),
                                            color=discord.Color.blurple())
            embed.set_footer(text="Moderation • Ban")
            await i.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))