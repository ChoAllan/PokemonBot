import os
import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import mysql.connector


load_dotenv()
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASS = os.getenv('PASS')
DATABASE = os.getenv('DATABASE')
class Catch(commands.Cog):


    def __init__(self, bot, number, name):
        self.bot = bot
        self.number = number
        self.name = name

    @commands.command(name="catch")
    async def catch(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        self.number = coinflip()
        print(self.number)
        if self.number == 0 :
            await ctx.send("Pokemon has been caught")
            mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASS,
            database=DATABASE
            )
            mycursor = mydb.cursor()
            try:
                sql = "INSERT INTO " + self.name + " (name) VALUES (%s)"
                print(self.name)
                val = (number)
                mycursor.execute(sql, val)

                mydb.commit()

            except:
                "error"
        elif self.number == 1:
            await ctx.send("Pokemon has not been caught")
    
def coinflip():
    return random.randint(0, 1)





# Testing for catch
# bot = commands.Bot(command_prefix='!')
# catch = Catch(bot, 3)
# print(getNo())