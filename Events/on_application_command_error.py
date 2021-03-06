import discord
from discord.ext import commands
from config import EMOTES, COLORS
import datetime
import traceback

class OnApplicationCmdError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            
            x = EMOTES["error"]
            Embed = discord.Embed(description=f"{x} This command is on cooldown", color=COLORS["error"])
            await ctx.respond(embed=Embed, ephemeral=True)
        
        else:
            x = EMOTES["error"]
            Embed = discord.Embed(description=f"{x} Something went wrong\n\n```py\n{error}```", color=COLORS["error"])
            await ctx.respond(embed=Embed)


def setup(bot):
    bot.add_cog(OnApplicationCmdError(bot))