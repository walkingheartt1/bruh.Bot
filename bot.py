import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='bruh')


@bot.event
async def on_ready():
    print("走心機器人 is online")

bot.run('Nzk3MDc3NDYzOTg4OTYxMzEx.X_hOPA.LgBsBuvDtP0s9Y3R7dHSslf6kS4')
