from pokedex import pokedex
import random

# randomly generates a pokemon from api
class Pokemon:
    def __init__(self):
        self.pokedex = pokedex.Pokedex()

    def getPokemon(self):
        number = random.randrange(0, 808)
        pokemon = self.pokedex.get_pokemon_by_number(number)
        return pokemon

# returns the name of the pokemon generated
def getName(pokemon):
        return pokemon[0].get('name')


# returns the sprite of the pokemon generated 
def getSprite(pokemon):
        return pokemon[0].get('sprite')

# # testing to generate pokemon
# pokemon = Pokemon()
# poke = pokemon.getPokemon()
# print(getName(poke))
# print(getSprite(poke))