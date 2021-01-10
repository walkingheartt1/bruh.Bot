import json
import random

import discord
from discord.ext import commands

with open('setting.json', mode='r', encoding='utf8') as location:
    diict = json.load(location)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='bruh-', intents=intents)


@bot.event
async def on_ready():
    print("走心機器人 is online")


@bot.event
async def on_member_join(member):
    print(F'{member}來啦!')


@bot.event
async def on_member_remove(member):
    print(F'{member}走了!')


bot.run(diict['Token'])
