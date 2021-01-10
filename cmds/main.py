import discord
from core.classes import Cog_Extention
from discord.ext import commands


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def ping(self, ctx):
            await ctx.send(F'{round(self.bot.latency*1000)}ms')


def setup(bot):
    bot.add_cog(Main(bot))
