# bot.py
import discord
import os
import random
import mysql.connector
from pokemondb import Pokemon
from pokemondb import *
from dotenv import load_dotenv
from discord.ext import commands
from catchCommand import Catch
from catchCommand import *

pokemon = Pokemon()

#read dotenv file in the same folder as python file
load_dotenv()
# takes token to connect to server
TOKEN = os.getenv('DISCORD_TOKEN')
# takes name guild server 
GUILD = os.getenv('DISCORD_GUILD')

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASS = os.getenv('PASS')
DATABASE = os.getenv('DATABASE')

# initalizes bot command as !
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
# bot.add_cog(Catch(bot, 0))


@bot.command(name="play")
async def play(ctx):

    name = str(ctx.message.author)
    newName = name.replace("#", '')
    # print(newName)
    bot.add_cog(Catch(bot, 0, newName))

    mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASS,
    database=DATABASE
    )

    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE TABLE "+newName+" (name VARCHAR(255))")
        await ctx.send(newName + " has arrived!")
    except:
        await ctx.send(newName + " has arrived!")
    


    # displays pokemon name and sprite
    poke = pokemon.getPokemon()
    
    
    response = "Let's play Pokemon!\n!Catch pokemon you see."
    name = poke['name']
    names = "A wild " + name + " has appeared!"
    sprite = poke['sprites']['back_default']
    await ctx.send(response)
    await ctx.send(sprite)
    await ctx.send(names)




# need this so bot can run
# client.run(TOKEN)
bot.run(TOKEN)







# # tracks messages in chat 
# @client.event
# async def on_message(message):
#     # determines if the message is from bot 
#     if message.author==client.user:
#         return

#     if message.content.lower() == "!play":
#         response = "Let's Play Pokemon"
#         # await message.channel.send(response) 
#         await bot.process_commands(response) 
#     # # how to raise exception
#     # elif message.content == 'raise-exception':
#     #     raise discord.DiscordException  

# client = discord.Client()
# # connects bot to server and determine who is in the server 
# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )
