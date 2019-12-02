from Game.Battle.Calculations import CalcAttack
from Game.Data.Pokedex import GetPokemon
from random import choice


def Attack(your_pokemon, opponent_pokemon, move):
    your_attack = CalcAttack(your_pokemon, opponent_pokemon, move)

    opponent_move = GetRandomMove(opponent_pokemon.moves)
    opponent_attack = CalcAttack(opponent_pokemon, your_pokemon, opponent_move)

    your_pokemon.hp = max(0, your_pokemon.hp - opponent_attack["damage"])
    print("%s uses %s." % (GetPokemon(opponent_pokemon.number)["name"].capitalize() if not opponent_pokemon.name else opponent_pokemon.name, opponent_move))
    for i in opponent_attack["messages"]:
        print(i)

    opponent_pokemon.hp = max(0, opponent_pokemon.hp - your_attack["damage"])
    print("%s uses %s." % (GetPokemon(your_pokemon.number)["name"].capitalize() if not your_pokemon.name else your_pokemon.name, move))
    for i in your_attack["messages"]:
        print(i)


def GetRandomMove(moves):
    return choice([i for i in moves if i is not None])
