# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    print(f"Game Initialized: {pygame.get_init()}")

## Set Variables For Game

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

## Main Game Loop
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
        dt = 1000/clock.tick(60)

if __name__ == "__main__":
    main()