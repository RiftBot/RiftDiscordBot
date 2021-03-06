import discord
from discord.ext import commands
import datetime
today = datetime.datetime.today()
from discord.ext.commands import MissingPermissions
class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member=None, *, reason=None):
        if reason == None and member == None:
            embed = discord.Embed(title="Error!", description="This command has not been ran properly.\ne.g !kick @member reason", color=discord.Color.red())
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title="Success!", description="The member has been kicked!", color=discord.Color.green())
            embed.add_field(name="Member", value=f"{member.mention}", inline=False)
            embed.add_field(name="Reason", value=f"{reason}", inline=False)
            embed.set_footer(text=f"{today}")
            await ctx.send(embed=embed)
            memberEmbed = discord.Embed(title="Kicked!", description=f"You have been kicked from guild {ctx.guild.name}", color=discord.Color.red())
            memberEmbed.add_field(name="Staff Member", value=f"{ctx.author.mention}", inline=False)
            memberEmbed.add_field(name="Reason", value=f"{reason}", inline=False)
            memberEmbed.set_footer(text=f"{today}", icon_url=f"{ctx.guild.icon_url}")
            try:
                await member.send(embed=memberEmbed)
                await member.kick(reason=reason)
            except Exception:
                embed = discord.Embed(title="Error!", description="Sorry but the embed could not be sent to the member!", color=discord.Color.red())
                await ctx.send(embed=embed)
                await member.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title="Error!", description="The command has ran into a error!", color=discord.Color.red())
            embed.add_field(name="Missing Permissions", value="You don't have the right permission to run this command!\nYou are missing `KICK_MEMBERS` permission.", inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member=None, *, reason=None):
        if reason == None and member == None:
            embed = discord.Embed(title="Error!", description="This command has not been ran properly.\ne.g !ban @member reason", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Success!", description="The member has been banned!", color=discord.Color.green())
            embed.add_field(name="Mmeber", value=f"{member.mention}", inline=False)
            embed.add_field(name="Reason", value=f"{reason}", inline=False)
            embed.set_footer(text=f"{today}")
            await ctx.send(embed=embed)
            memberEmbed = discord.Embed(title="Kicked!", description=f"You have been banned from guild {ctx.guild.name}", color=discord.Color.red())
            memberEmbed.add_field(name="Staff Member", value=f"{ctx.author.mention}", inline=False)
            memberEmbed.add_field(name="Reason", value=f"{reason}", inline=False)
            memberEmbed.set_footer(text=f"{today}", icon_url=f"{ctx.guild.icon_url}")
            try:
                await member.send(embed=memberEmbed)
                await member.ban(reason=reason)
            except Exception:
                embed = discord.Embed(title="Error!", description="Sorry but the embed could not be sent to the member!", color=discord.Color.red())
                await ctx.send(embed=embed)
                await member.ban(reason=reason)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title="Error!", description="The command ran into an error!", color=discord.Color.red())
            embed.add_field(name="Missing Permissions", value="You don't have the right permission to run this command!\nYou are missing `BAN_MEMBERS` permission")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))
