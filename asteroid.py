from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        position = (int(self.position.x),int(self.position.y))
        pygame.draw.circle(screen,"white", position, self.radius, 2)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)