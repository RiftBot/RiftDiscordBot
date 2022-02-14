import discord
from discord.ext import commands
import config
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot is logged in!")

bot.run(config.token)
