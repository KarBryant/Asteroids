import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    """
    Represents a projectile shot in the game, inheriting from CircleShape.

    Attributes:
        position (pygame.Vector2): Current position of the shot.
        velocity (pygame.Vector2): Velocity vector determining shot movement.
        radius (int): Radius of the shot circle.
    """

    def __init__(self, x, y, radius):
        """
        Initialize a Shot object at the given position with the specified radius.

        Args:
            x (float): Initial x-coordinate of the shot.
            y (float): Initial y-coordinate of the shot.
            radius (int): Radius of the shot's circular representation.
        """

        super().__init__(x, y, radius)

    def draw(self, screen):
        """
        Draw the shot as a white circle on the given Pygame screen.

        Args:
            screen (pygame.Surface): The surface to draw the shot on.
        """

        position = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", position, self.radius, 2)

    def update(self, delta_time):

        """
        Update the shot's position based on its velocity and elapsed time.

        Args:
            delta_time (float): Time elapsed since the last update (usually in milliseconds or seconds).
        """

        self.position += (self.velocity * delta_time)
