from math import floor
from pygame import image, font, draw


def HandleBattle(screen):
    DrawBackground(screen)
    DrawPlayerPokemon(screen)
    DrawOpponentPokemon(screen)
    DrawOptions(screen)


def DrawBackground(screen):
    background_image = image.load("Images/Battle/grass.png")
    screen.blit(background_image, (0, 0))


def DrawPlayerPokemon(screen):
    name = "Squirtle"
    image_index = 7
    level = 95
    percent_health = 0.75
    percent_experience = 0.4

    # Draw the Pokemon's info background
    draw.rect(screen, (62, 73, 65), (118, 78, 108, 35))         # Outline
    draw.rect(screen, (251, 252, 218), (119, 79, 106, 28))   # Content

    # Draw the health bar
    draw.rect(screen, (62, 73, 65), (148, 98, 72, 4))
    draw.rect(screen, (131, 213, 164), (148, 98, floor(percent_health * 72), 4))

    # Draw the experience bar
    draw.rect(screen, (191, 186, 154), (136, 109, 84, 2))
    draw.rect(screen, (77, 200, 234), (136, 109, floor(percent_experience * 84), 2))

    # Print the Pokemon's name
    my_font = font.SysFont(None, 15)
    name_label = my_font.render(name, 1, (0, 0, 0))
    screen.blit(name_label, (122, 84))

    # Print the Pokemon's level
    my_font = font.SysFont(None, 15)
    level_label = my_font.render("Lv: " + str(level), 1, (0, 0, 0))
    screen.blit(level_label, (186, 84))

    # Draw the Pokemon
    sprite_sheet = image.load("Images/Pokemon/pokemon-back.png")
    DrawPokemon(screen, sprite_sheet, 32, 64, image_index)


def DrawOpponentPokemon(screen):
    name = "Bulbasaur"
    image_index = 1                                         # Bulbasaur's number
    level = 100
    percent_health = 0.5

    # Draw the Pokemon's info background
    draw.rect(screen, (62, 73, 65), (14, 14, 108, 32))         # Outline
    draw.rect(screen, (251, 252, 218), (15, 15, 106, 30))   # Content

    # Draw the health bar
    draw.rect(screen, (62, 73, 65), (44, 34, 72, 4))
    draw.rect(screen, (131, 213, 164), (44, 34, floor(percent_health * 72), 4))

    # Print the Pokemon's name
    my_font = font.SysFont(None, 15)
    name_label = my_font.render(name, 1, (0, 0, 0))
    screen.blit(name_label, (18, 20))

    # Print the Pokemon's level
    my_font = font.SysFont(None, 15)
    level_label = my_font.render("Lv: " + str(level), 1, (0, 0, 0))
    screen.blit(level_label, (82, 20))

    # Draw the Pokemon
    sprite_sheet = image.load("Images/Pokemon/pokemon.png")
    DrawPokemon(screen, sprite_sheet, 138, 16, image_index)


def DrawOptions(screen):
    draw.rect(screen, (62, 73, 65), (0, 113, 240, 47))
    draw.rect(screen, (205, 177, 80), (2, 115, 236, 43))
    draw.rect(screen, (185, 196, 198), (5, 118, 230, 37))
    draw.rect(screen, (48, 78, 102), (5, 119, 228, 35))


def DrawPokemon(screen, sprite_sheet, x, y, index):
    rows = 16
    columns = 25
    image_width = sprite_sheet.get_rect().size[0]
    image_height = sprite_sheet.get_rect().size[1]
    width = image_width / columns
    height = image_height / rows

    screen.blit(
        sprite_sheet,
        (x, y),
        (
            width * ((index - 1) % columns),
            height * floor(index / (columns + 1)),
            width,
            height
        )
    )
