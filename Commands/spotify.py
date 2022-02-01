from discord.ext import commands
from discord.commands import Option, slash_command
import discord
from config import COLORS, EMOTES
import datetime

class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def spotify(self, ctx: commands.Context, member: Option(discord.Member, "Select a user", required=False, default=None)):
        """Get Spotify stats of someone or yourself"""

        await ctx.defer()

        if member == None:
            id = ctx.author.id
        elif type(member) == int:
            id = member
        else:
            id = member.id

        user = ctx.guild.get_member(id)

        if user is not None:
    

         try:
             avatar = user.display_avatar.url
             emoji = EMOTES["spotify"]

             Embed = discord.Embed(description=f"{user.mention} | {emoji}", timestamp=datetime.datetime.utcnow(), color=user.color)
             Embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=avatar)

             Embed.set_thumbnail(url=user.activity.album_cover_url)

             artists = user.activity.artists
             duration = user.activity.duration
             durationd = str(duration).split(".")[0]

             Embed.add_field(name="Song", value=user.activity.title, inline=False)
             Embed.add_field(name="Duration", value=durationd, inline=True)
             Embed.add_field(name="Artist", value=", ".join(artists), inline=False)
             Embed.add_field(name="Album", value=user.activity.album, inline=True)


             Embed.set_footer(text=f"ID: {user.id}", icon_url="https://emoji.gg/assets/emoji/7370_Spotify.png")


             View = discord.ui.View()
             View.add_item(discord.ui.Button(emoji=emoji,label='Listen on Spotify', url=user.activity.track_url, style=discord.ButtonStyle.url))

             await ctx.respond(embed=Embed, view=View)


         except Exception:
             error = EMOTES["error"]
             Embed = discord.Embed(description=f"{error} This user is not listening to Spotify", color=COLORS["error"])
             await ctx.respond(embed=Embed)

        else:
             error = EMOTES["error"]
             Embed = discord.Embed(description=f"{error} Couldn't find this member", color=COLORS["error"])
             await ctx.respond(embed=Embed)

def setup(bot):
    bot.add_cog(Spotify(bot))
