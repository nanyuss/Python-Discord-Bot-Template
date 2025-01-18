import discord
from discord.ext import commands

from ...bot import MyBot

class Owner(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot: MyBot = bot

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send('Funcionando!')

async def setup(bot: MyBot):
    await bot.add_cog(Owner(bot))