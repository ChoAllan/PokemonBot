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
                url = pokemon.url

                req = Request(
                        url=url, 
                        headers={'User-Agent': 'Mozilla/5.0'}
                        )
                response = urlopen(req)

                data_json = json.loads(response.read()) 

                return data_json


