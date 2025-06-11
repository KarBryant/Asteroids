from circleshape import CircleShape
import pygame
import constants
import random


class Asteroid(CircleShape):
    """
    A game object representing an asteroid that can move, be drawn,
    and split into smaller asteroids upon destruction.
    """

    def __init__(self, x, y, radius):
        """
        Initialize an asteroid at a given position and size.

        Args:
            x (float): The initial x-coordinate of the asteroid.
            y (float): The initial y-coordinate of the asteroid.
            radius (int or float): The radius of the asteroid.
        """

        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draw the asteroid as a white circle on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the asteroid on.
        """

        position = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", position, self.radius, 2)

    def update(self, delta_time):
        """
        Update the asteroid's position based on its velocity and elapsed time.

        Args:
            delta_time (float): Time since the last update.
        """

        self.position += (self.velocity * delta_time)

    def split(self):
        """
        Split the asteroid into two smaller asteroids if it's large enough.

        - Increases the player's score.
        - If the asteroid is too small, it is simply destroyed.
        - Otherwise, two new smaller asteroids are spawned with rotated velocities.
        """
        
        self.kill()
        constants.PLAYER_SCORE += 10
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        new_asteroid_a_angle = self.velocity.rotate(random_angle)
        new_asteroid_b_angle = self.velocity.rotate(-random_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        new_astroid_a = Asteroid(self.position[0], self.position[1], new_radius)
        new_astroid_b = Asteroid(self.position[0], self.position[1], new_radius)
        new_astroid_a.velocity = new_asteroid_a_angle
        new_astroid_b.velocity = new_asteroid_b_angle
