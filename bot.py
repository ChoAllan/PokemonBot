# bot.py
import os
import random
from pokemondb import Pokemon
from pokemondb import getName
from pokemondb import getSprite

import discord
from dotenv import load_dotenv

from discord.ext import commands

pokemon = Pokemon()

#read dotenv file in the same folder as python file
load_dotenv()
# takes token to connect to server
TOKEN = os.getenv('DISCORD_TOKEN')
# takes name guild server 
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
# connects bot to server and determine who is in the server 
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )



# tracks messages in chat 
@client.event
async def on_message(message):
    # determines if the message is from bot 
    if message.author==client.user:
        return

    if message.content.lower() == "!play":
        response = "Let's Play Pokemon"
        # await message.channel.send(response) 
        await bot.process_commands(response) 
    # # how to raise exception
    # elif message.content == 'raise-exception':
    #     raise discord.DiscordException  

bot = commands.Bot(command_prefix='!')


@bot.command(name="play")
async def play(ctx):

    # displays pokemon name and sprite
    poke = pokemon.getPokemon()
    
    response = "Let's play Pokemon!"
    name = getName(poke)
    sprite = getSprite(poke)
    await ctx.send(response)
    await ctx.send(sprite)
    await ctx.send(name)

    
    



# need this so bot can run
# client.run(TOKEN)
bot.run(TOKEN)