from random import choice, randint
from Game.Data.Pokedex import GetPokemon


class Pokemon:
    def __init__(self, number, level):
        self.name = None

        self.number = number
        self.level = level
        self.iv = randint(0, 31)
        self.ev = 0
        self.base_pokemon = GetPokemon(number)

        self.max_hp, self.attack, self.defense, self.sp_attack, self.sp_defense, self.speed = 0, 0, 0, 0, 0, 0
        self.UpdateStats()
        self.hp = self.max_hp

        self.exp = 413
        self.max_exp = 1112

        self.moves = [None, None, None, None]

        for i in range(1, self.level):
            if i in self.base_pokemon["moves"]:
                full = self.moves[0] and self.moves[1] and self.moves[2] and self.moves[3]
                random = randint(0, 3)

                if self.moves[0] is None or (full and random == 0):
                    self.moves[0] = self.base_pokemon["moves"][i]
                elif self.moves[1] is None or (full and random == 1):
                    self.moves[1] = self.base_pokemon["moves"][i]
                elif self.moves[2] is None or (full and random == 2):
                    self.moves[2] = self.base_pokemon["moves"][i]
                else:
                    self.moves[3] = self.base_pokemon["moves"][i]

    def LevelUp(self):
        self.UpdateStats()

    def UpdateStats(self):
        self.max_hp = (((2 * (self.base_pokemon["stats"]["hp"]) + self.iv + (
                    self.ev / 4) + 100) * self.level) / 100) + 10
        self.attack = (((2 * (self.base_pokemon["stats"]["attack"]) + self.iv + (
                    self.ev / 4) + 100) * self.level) / 100) + 10
        self.defense = (((2 * (self.base_pokemon["stats"]["defense"]) + self.iv + (
                    self.ev / 4) + 100) * self.level) / 100) + 10
        self.sp_attack = (((2 * (self.base_pokemon["stats"]["special_attack"]) + self.iv + (
                    self.ev / 4) + 100) * self.level) / 100) + 10
        self.sp_defense = (((2 * (self.base_pokemon["stats"]["special_defense"]) + self.iv + (
                    self.ev / 4) + 100) * self.level) / 100) + 10
        self.speed = (((2 * (self.base_pokemon["stats"]["speed"]) + self.iv + (
                    self.ev / 4) + 100) * self.level) / 100) + 10


def CreatePokemon(pokemon, min_level, max_level):
    return Pokemon(choice(pokemon), randint(min_level, max_level))
