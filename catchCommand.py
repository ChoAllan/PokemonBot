import discord
from discord.ext import commands
import random

class Catch(commands.Cog):
    def __init__(self, bot, number):
        self.bot = bot
        self.number = number

    def coinflip(self):
        return random.randint(0, 1)

    @commands.command(name="catch")
    async def catch(self, ctx, *, member: discord.Member = None):
        memmber = member or ctx.author
        if coinflip() == 0 :
            await ctx.send("Pokemon has been caught")
        elif coinflip == 1:
            await ctx.send("Pokemon has not been caught")
    

def getNo(Catch):
    return catch.number



# Testing for catch
# bot = commands.Bot(command_prefix='!')
# catch = Catch(bot, 3)
# print(getNo())