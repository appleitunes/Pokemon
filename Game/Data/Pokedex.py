import requests
import json


pokedex = {}


# https://pokeapi.co/docs/v2.html
def GetPokemon(identifier):
    identifier = identifier.lower() if isinstance(identifier, str) else identifier
    if identifier not in pokedex:
        raw_data_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/%s" % identifier)
        parsed_data_pokemon = json.loads(raw_data_pokemon.content)
        pokemon_data = {
            "name": parsed_data_pokemon["name"],
            "id": parsed_data_pokemon["id"],
            "types": [
                i["type"]["name"]
                for i in parsed_data_pokemon["types"]
            ],
            "stats": {
                "speed": parsed_data_pokemon["stats"][0]["base_stat"],
                "special_defense": parsed_data_pokemon["stats"][1]["base_stat"],
                "special_attack": parsed_data_pokemon["stats"][2]["base_stat"],
                "defense": parsed_data_pokemon["stats"][3]["base_stat"],
                "attack": parsed_data_pokemon["stats"][4]["base_stat"],
                "hp": parsed_data_pokemon["stats"][5]["base_stat"]
            },
            "moves": {
                i["version_group_details"][0]["level_learned_at"]: i["move"]["name"]
                for i in parsed_data_pokemon["moves"]
            }
        }
        pokedex[pokemon_data["name"]] = pokemon_data
        pokedex[pokemon_data["id"]] = pokemon_data
    return pokedex[identifier]
