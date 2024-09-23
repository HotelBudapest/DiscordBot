import discord
from discord.ext import commands
import random

class Toss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def toss(self, ctx):
        stuff = ["Heads", "Tails"]
        index = random.randint(0,1)
        await ctx.send(f"You have got: {stuff[index]}")

    @commands.command()
    async def dice_roll(self, ctx):
        await ctx.send(f"You have rolled: {random.randint(1,6)}")


async def setup(bot):
    await bot.add_cog(Toss(bot))
    print("Toss and Dice cog loaded")