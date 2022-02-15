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


    @commands.command()
    async def userinfo(self, ctx, member : discord.Member=None):
        if member is None:
            created_at = ctx.author.created_at.strftime("%b %d, %Y")
            joined_at = ctx.author.joined_at.strftime("%b %d, %Y")
            embed = discord.Embed(title="User Information", description=f"User information about {ctx.author.mention}", color=discord.Color.green())
            embed.add_field(name="Username", value=f"{ctx.author.mention}", inline=False)
            embed.add_field(name="Tag", value=f"{ctx.author.discriminator}", inline=False)
            embed.add_field(name="Joined In", value=f"{joined_at}", inline=False)
            embed.add_field(name="User Created", value=f"{created_at}", inline=False)
            embed.set_image(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            created_at = member.created_at.strftime("%b %d, %Y")
            joined_at = member.joined_at.strftime("%b %d, %Y")
            embed = discord.Embed(title="User Information", description=f"User information about {member.mention}", color=discord.Color.green())
            embed.add_field(name="Username", value=f"{member.mention}", inline=False)
            embed.add_field(name="Tag", value=f"{member.discriminator}", inline=False)
            embed.add_field(name="Joined In", value=f"{joined_at}", inline=False)
            embed.add_field(name="User Created", value=f"{created_at}", inline=False)
            embed.set_image(url=member.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        created_at = ctx.guild.created_at.strftime("%b %d, %Y")
        embed = discord.Embed(title="Server Information", description=f"Server information about {ctx.guild.name}", color=discord.Color.green())
        embed.add_field(name="Server Name", value=f"{ctx.guild.name}", inline=False)
        embed.add_field(name="Created", value=f"{created_at}", inline=False)
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
