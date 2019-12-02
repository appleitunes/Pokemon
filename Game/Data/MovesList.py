import requests
import json


moves_list = {}


# https://pokeapi.co/docs/v2.html
def GetMove(identifier):
    identifier = identifier.lower() if isinstance(identifier, str) else identifier
    if identifier not in moves_list:
        raw_data = requests.get("https://pokeapi.co/api/v2/move/%s" % identifier)
        parsed_data = json.loads(raw_data.content)
        move_data = {
            "name": parsed_data["name"],
            "id": parsed_data["id"],
            "accuracy": parsed_data["accuracy"],
            "pp": parsed_data["pp"],
            "power": parsed_data["power"],
            "type": parsed_data["type"]["name"],
            "critical_rate": parsed_data["meta"]["crit_rate"]
        }
        moves_list[move_data["name"]] = move_data
        moves_list[move_data["id"]] = move_data
    return moves_list[identifier]
