import discord
from discord.ext import commands
import platform
import psutil
import os
platform = platform.system()
class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = (load15/os.cpu_count()) * 100
        embed = discord.Embed(title="Bot Information", description="Information about the bot.", color=discord.Color.green())
        embed.add_field(name="Guilds", value=f"{len(self.bot.guilds)}", inline=False)
        embed.add_field(name="OS Name", value=f"{platform}", inline=False)
        embed.add_field(name="CPU Usage", value=f"{cpu_usage}", inline=False)
        embed.add_field(name="Number Of Commands", value="4", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
