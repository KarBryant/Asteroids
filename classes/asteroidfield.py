"""
Module for managing the spawning of asteroids in the game.

Contains the AsteroidField class, which periodically spawns Asteroid
objects at random edges of the screen with random movement vectors.
"""

import pygame
import random
from .asteroid import Asteroid
from constants import (ASTEROID_MAX_RADIUS,
                       SCREEN_HEIGHT,
                       SCREEN_WIDTH,
                       ASTEROID_SPAWN_RATE,
                       ASTEROID_MIN_RADIUS,
                       ASTEROID_KINDS)


class AsteroidField(pygame.sprite.Sprite):
    """
    Manages the automatic spawning of asteroids around the screen edges.

    Periodically spawns asteroids moving toward the center of the screen
    using randomized directions and sizes.
    """

    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        """
        Initialize the AsteroidField with a spawn timer.
        """

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Create a new asteroid and set its velocity.

        Args:
            radius (int): The size of the new asteroid.
            position (pygame.Vector2): The position to spawn the asteroid.
            velocity (pygame.Vector2): The direction and speed of the asteroid.
        """

        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Update the spawn timer and spawn a new asteroid if needed.

        Args:
            dt (float): Time delta in milliseconds since last update.
        """
        
        self.spawn_timer += dt / 1000
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(1, 2) / 100
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
