import discord
from discord.ext import commands
from config import EMOTES, COLORS
import datetime
import traceback

class OnCmdError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            
            x = EMOTES["error"]
            Embed = discord.Embed(description=f"{x} This command is on cooldown", color=COLORS["error"])
            await ctx.send(embed=Embed)

        elif isinstance(error, commands.MissingRequiredArgument):
            x = EMOTES["error"]
            arg = str(error)
            arg = arg.split(" ")

            Embed = discord.Embed(description=f"{x} Missing argument: `{arg[0]}`", color=COLORS["error"])
            await ctx.send(embed=Embed)

        elif isinstance(error, commands.CommandNotFound):
            pass

        else:
            x = EMOTES["error"]
            Embed = discord.Embed(description=f"{x} Something went wrong\n\n```py\n{error}```", color=COLORS["error"])
            await ctx.send(embed=Embed)


def setup(bot):
    bot.add_cog(OnCmdError(bot))
