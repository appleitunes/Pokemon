from Game.Data.Pokedex import GetPokemon
from Game.Data.MovesList import GetMove
from Game.Data.Types import GetType
from math import ceil, pow
from random import uniform


# https://bulbapedia.bulbagarden.net/wiki/Damage#Damage_calculation
def CalcAttack(attacker, defender, move):
    move_data = GetMove(move)
    move_power = move_data["power"]
    move_type = move_data["type"]
    critical_hit_rate = move_data["critical_rate"]

    if move_power is None:
        return {
            "damage": 0,
            "messages": []
        }

    attacking_pokemon_types = GetPokemon(attacker.number)["types"]
    defending_pokemon_types = GetPokemon(defender.number)["types"]

    type_data = GetType(move_type)
    double_damage_list = type_data["double_damage"]
    half_damage_list = type_data["half_damage"]
    no_damage_list = type_data["no_damage"]

    double_damage_count = len([i for i in defending_pokemon_types if i in double_damage_list])
    half_damage_count = len([i for i in defending_pokemon_types if i in half_damage_list])
    no_damage_count = len([i for i in defending_pokemon_types if i in no_damage_list])

    type_effectiveness = 0 if 0 != no_damage_count else 1 * pow(2, double_damage_count) * pow(0.5, half_damage_count)

    critical_hit = 2 if (uniform(0, 100) <= (6.25 if critical_hit_rate == 1 else 12.5)) else 1

    modifier = uniform(0.75, 1) * (1.5 if move_type in attacking_pokemon_types else 1) * type_effectiveness
    damage = ceil(((((2 * (attacker.level * critical_hit)) * move_power * (attacker.attack / defender.defense)) / 50) + 2) * modifier)

    messages = []

    if critical_hit == 2:
        messages.append("It's a critical hit!")

    if type_effectiveness < 1:
        messages.append("It's not very effective...")
    else:
        messages.append("It's super effective!")

    return {
        "damage": damage,
        "messages": messages
    }
