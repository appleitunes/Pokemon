import pygame
from Game.Battle.Battle import HandleBattle


pygame.init()
screen = pygame.display.set_mode((240, 160))


# Game loop
done = False
while not done:
    screen.fill((255, 255, 255))

    # End game loop if window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw battle
    HandleBattle(screen)

    pygame.display.flip()
