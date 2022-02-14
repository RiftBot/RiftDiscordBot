import discord
from discord.ext import commands
import config
import os
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot is logged in!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Loaded cog\n{filename[:-3]}\n")
    else:
        print(f"This file in the cogs folder does not end with .py!\n{filename[:-3]}\n")

bot.run(config.token)
