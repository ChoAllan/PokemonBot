import pokebase as pb
import random
import json

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
        return pokemon[0].get('name')


# returns the sprite of the pokemon generated 
def getSprite(pokemon):
        return pokemon[0].get('sprite')

# # testing to generate pokemon
pokemon = Pokemon()
poke = pokemon.getPokemon()
print(poke)
# print(getName(poke))
# print(getSprite(poke))
