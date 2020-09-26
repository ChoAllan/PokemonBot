import pytest
from pokemondb import Pokemon
from pokemondb import *
from pokedex import pokedex


# TEST pokemon no.1 is the right pokemon
def test_pokemondb_getName():
    pokedexs = pokedex.Pokedex()
    pokemon = Pokemon()
    pokemon1 = pokedexs.get_pokemon_by_number(1)
    name1 = getName(pokemon1)
    assert name1 == "Bulbasaur", "name failed"
def test_pokemondb_getSprite():
    pokedexs = pokedex.Pokedex()
    pokemon = Pokemon()
    pokemon1 = pokedexs.get_pokemon_by_number(1)
    sprite = getSprite(pokemon1)
    assert sprite == "https://cdn.traction.one/pokedex/pokemon/1.png", "sprite failed"



# TEST pokemon no. 808 is out of bounds
def test_pokemondb_noName():
    pokedexs = pokedex.Pokedex()
    pokemon = Pokemon()
    try:
        pokemon1 = pokedexs.get_pokemon_by_number(808)
        name1 = getName(pokemon1)
    except:
        name1 = ""
    assert name1 == "", "name failed"

def test_pokemondb_noSprite():
    pokedexs = pokedex.Pokedex()
    pokemon = Pokemon()
    try:
        pokemon1 = pokedexs.get_pokemon_by_number(808)
        sprite = getSprite(pokemon1)
    except:
        sprite = ""
    assert sprite == "", "sprite failed"



# TEST pokemon no. 0 is out of bounds
def test_pokemondb_noName0():
    pokedexs = pokedex.Pokedex()
    pokemon = Pokemon()
    try:
        pokemon1 = pokedexs.get_pokemon_by_number(0)
        name1 = getName(pokemon1)
    except:
        name1 = ""
    assert name1 == "", "name failed"

def test_pokemondb_noSprite0():
    pokedexs = pokedex.Pokedex()
    pokemon = Pokemon()
    try:
        pokemon1 = pokedexs.get_pokemon_by_number(0)
        sprite = getSprite(pokemon1)
    except:
        sprite = ""
    assert sprite == "", "sprite failed"

