import requests
import json


types_list = {}


# https://pokeapi.co/docs/v2.html#types
def GetType(identifier):
    identifier = identifier.lower() if isinstance(identifier, str) else identifier
    if identifier not in types_list:
        raw_data = requests.get("https://pokeapi.co/api/v2/type/%s" % identifier)
        parsed_data = json.loads(raw_data.content)
        type_data = {
            "name": parsed_data["name"],
            "id": parsed_data["id"],
            "no_damage": [i["name"] for i in parsed_data["damage_relations"]["no_damage_to"]],
            "half_damage": [i["name"] for i in parsed_data["damage_relations"]["half_damage_to"]],
            "double_damage": [i["name"]for i in parsed_data["damage_relations"]["double_damage_to"]]
        }
        types_list[type_data["name"]] = type_data
        types_list[type_data["id"]] = type_data
    return types_list[identifier]
