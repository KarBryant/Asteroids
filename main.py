"""
This module initializes the game, sets up game objects and groups,
and runs the main game loop. It handles events, updates game state,
checks collisions, and renders the game screen each frame.
"""

import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from ScoreDisplay import ScoreDisplay


def main():
    """
    Entry point for the Asteroids game.

    Initializes pygame, creates game objects and sprite groups,
    then enters the main loop which handles events, updates objects,
    detects collisions, renders graphics, and tracks the player's score.
    """

    # Game Initilaization
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    print(f"Game Initialized: {pygame.get_init()}")

    # Set Variables For Game
    clock = pygame.time.Clock()
    dt = 0  # Delta-Time
    screen = pygame.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    )
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2

    # Groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Group Initilization
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables, )
    Shot.containers = (updatables, drawables, shots)

    # Objects
    player = Player(x, y)
    AsteroidField()
    score_element = ScoreDisplay(64, (0, 0))

    # Main Game Loop
    while pygame.get_init():
        dt = 1000 / clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for asteroid in asteroids:
            if asteroid.has_collided(player):
                constants.PLAYER_SCORE = 0
                print("Game Over!")
                pygame.quit()
                raise Exception(SystemExit)

            for shot in shots:
                if shot.has_collided(asteroid):
                    asteroid.split()
                    shot.kill()

        updatables.update(dt)

        for sprite in drawables:
            sprite.draw(screen)

        score_element.render(screen, constants.PLAYER_SCORE)
        pygame.display.flip()


if __name__ == "__main__":
    main()
