from circleshape import CircleShape
import pygame
import constants
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        position = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", position, self.radius, 2)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)

    def split(self):
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
