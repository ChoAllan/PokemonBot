import pokebase as pb
import random
import json
from urllib.request import urlopen, Request


# randomly generates a pokemon from api
class Pokemon:
    def __init__(self):
        self.pb = pb

    def getPokemon(self):
        number = random.randrange(0, 808)
        pokemon = self.pb.pokemon(number)
        return pokemon

# returns the name of the pokemon generated
def getName(pokemon):
        pokemon


# returns the sprite of the pokemon generated 
def getSprite(pokemon):
        return pokemon[0].get('sprite')

# # testing to generate pokemon
pokemon = Pokemon()
poke = pokemon.getPokemon()
url = poke.url
print(url)

req = Request(
    url=url, 
    headers={'User-Agent': 'Mozilla/5.0'}
)
response = urlopen(req)

data_json = json.loads(response.read()) 

print(data_json) 
# print(getName(poke))
# print(getSprite(poke))
