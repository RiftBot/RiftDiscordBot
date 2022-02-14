import discord
from discord.ext import commands
import time
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        ping = (time.monotonic() - before) * 1000
        embed = discord.Embed(title="Pong!")
        embed.add_field(name="Ping pong!", value=f"{int(ping)}ms")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(General(bot))
