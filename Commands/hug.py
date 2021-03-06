from discord.commands import slash_command, Option
from discord.ext import commands
import requests
import discord
import datetime

class Hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Hug a user you mention"
        self.category = "Fun"

    @slash_command()
    async def hug(self, ctx: commands.Context, user: Option(discord.Member, "Select a user")):
        """Hug someone"""
        
        request = requests.get("https://some-random-api.ml/animu/hug").json()
        image = request["link"]

        Embed = discord.Embed(
            description=f"{ctx.author.mention} hugs {user.mention}. uwu",
            timestamp=datetime.datetime.utcnow(),
            color=user.color
        )

        Embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=f"{user.avatar.url}")
        Embed.set_image(url=f"{image}")

        Embed.set_footer(text=f"From {ctx.user}")
        
        await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Hug(bot))
