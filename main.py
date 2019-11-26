from math import floor
from random import randint as rand

Natures = []

Pikachu = {
    'Stats': {
        'HP': [35, rand(0, 31)],
        'Attack': [55, rand(0, 31)],
        'Defense': [40, rand(0, 31)],
        'Sp Attack': [50, rand(0, 31)],
        'Sp Defense': [50, rand(0, 31)],
        'Speed': [90, rand(0, 31)]
    },
    'Level': 35,
    'Effort Value': 0
}


def calcStat(B, IV, EV, L, N):
    # B - Base Stat
    # IV - Individual Value
    # EV - Effort Value
    # L - Level
    # N - Nature
    return floor(floor((2 * B + IV + EV) * L / 100 + 5) * N)
