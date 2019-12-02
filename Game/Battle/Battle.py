from math import floor
from random import choice
from pygame import image, font, draw, K_SPACE, KEYDOWN, event as key_events
from Game.Data.Pokedex import GetPokemon
from Game.Data.Pokemon import CreatePokemon
from Game.Battle.Actions import Attack


your_pokemon = CreatePokemon([3, 6, 9], 30, 50)
opponent_pokemon = CreatePokemon([3, 6, 9], 30, 50)


def HandleBattle(screen):
    DrawBackground(screen)
    DrawPlayerPokemon(screen, your_pokemon)
    DrawOpponentPokemon(screen, opponent_pokemon)
    DrawOptions(screen, your_pokemon)

    events = key_events.get()
    for event in events:
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                Attack(your_pokemon, opponent_pokemon, choice(your_pokemon.moves))


def DrawBackground(screen):
    background_image = image.load("Images/Battle/grass.png")
    screen.blit(background_image, (0, 0))


def DrawPlayerPokemon(screen, pokemon):
    name = pokemon.name if pokemon.name else GetPokemon(pokemon.number)["name"].capitalize()
    image_index = pokemon.number
    level = pokemon.level
    percent_health = pokemon.hp / pokemon.max_hp
    percent_experience = pokemon.exp / pokemon.max_exp

    # Draw the Pokemon's info background
    draw.rect(screen, (62, 73, 65), (118, 78, 108, 35))         # Outline
    draw.rect(screen, (251, 252, 218), (119, 79, 106, 28))      # Content

    # Draw the health bar
    draw.rect(screen, (62, 73, 65), (148, 98, 72, 4))
    draw.rect(screen, (131, 213, 164), (148, 98, floor(percent_health * 72), 4))

    # Draw the experience bar
    draw.rect(screen, (191, 186, 154), (136, 109, 84, 2))
    draw.rect(screen, (77, 200, 234), (136, 109, floor(percent_experience * 84), 2))

    # Set the font
    my_font = font.SysFont(None, 15)

    # Print the Pokemon's name
    name_label = my_font.render(name, 1, (0, 0, 0))
    screen.blit(name_label, (122, 84))

    # Print the Pokemon's level
    level_label = my_font.render("Lv: " + str(level), 1, (0, 0, 0))
    screen.blit(level_label, (186, 84))

    # Draw the Pokemon
    sprite_sheet = image.load("Images/Pokemon/pokemon-back.png")
    DrawPokemon(screen, sprite_sheet, 32, 64, image_index)


def DrawOpponentPokemon(screen, pokemon):
    name = pokemon.name if pokemon.name else GetPokemon(pokemon.number)["name"].capitalize()
    image_index = pokemon.number
    level = pokemon.level
    percent_health = pokemon.hp / pokemon.max_hp

    # Draw the Pokemon's info background
    draw.rect(screen, (62, 73, 65), (14, 14, 108, 32))          # Outline
    draw.rect(screen, (251, 252, 218), (15, 15, 106, 30))       # Content

    # Draw the health bar
    draw.rect(screen, (62, 73, 65), (44, 34, 72, 4))
    draw.rect(screen, (131, 213, 164), (44, 34, floor(percent_health * 72), 4))

    # Set the font
    my_font = font.SysFont(None, 15)

    # Print the Pokemon's name
    name_label = my_font.render(name, 1, (0, 0, 0))
    screen.blit(name_label, (18, 20))

    # Print the Pokemon's level
    level_label = my_font.render("Lv: " + str(level), 1, (0, 0, 0))
    screen.blit(level_label, (82, 20))

    # Draw the Pokemon
    sprite_sheet = image.load("Images/Pokemon/pokemon.png")
    DrawPokemon(screen, sprite_sheet, 138, 12, image_index)


def DrawOptions(screen, pokemon):
    draw.rect(screen, (62, 73, 65), (0, 113, 240, 47))
    draw.rect(screen, (205, 177, 80), (2, 115, 236, 43))
    draw.rect(screen, (185, 196, 198), (5, 118, 230, 37))
    draw.rect(screen, (48, 78, 102), (5, 119, 228, 35))

    # Set the font
    my_font = font.SysFont(None, 15)

    # Draw first move
    level_label = my_font.render(pokemon.moves[0] if pokemon.moves[0] else "-", 1, (255, 255, 255))
    screen.blit(level_label, (18, 124))

    # Draw second move
    level_label = my_font.render(pokemon.moves[1] if pokemon.moves[1] else "-", 1, (255, 255, 255))
    screen.blit(level_label, (90, 124))

    # Draw third move
    level_label = my_font.render(pokemon.moves[2] if pokemon.moves[2] else "-", 1, (255, 255, 255))
    screen.blit(level_label, (18, 138))

    # Draw last move
    level_label = my_font.render(pokemon.moves[3] if pokemon.moves[3] else "-", 1, (255, 255, 255))
    screen.blit(level_label, (90, 138))


def DrawPokemon(screen, sprite_sheet, x, y, index):
    rows = 16
    columns = 25
    image_width = sprite_sheet.get_rect().size[0]
    image_height = sprite_sheet.get_rect().size[1]
    width = image_width / columns
    height = image_height / rows
    index -= 1

    screen.blit(
        sprite_sheet,
        (x, y),
        (
            width * (index % columns),
            height * floor(index / columns),
            width,
            height
        )
    )
