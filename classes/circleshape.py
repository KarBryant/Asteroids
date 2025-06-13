import pygame


class CircleShape(pygame.sprite.Sprite):
    """
    Base class for circular game objects with position, velocity, and radius.

    Provides a common structure for objects that move and can collide,
    such as player shots or asteroids.
    """

    def __init__(self, x, y, radius):
        """
        Initialize a circular object with position, zero velocity, and a radius.

        Args:
            x (float): X-coordinate of the object's position.
            y (float): Y-coordinate of the object's position.
            radius (int or float): Radius of the circle.
        """

        if hasattr(self, "containers"):
            super().__init__(self.containers)

        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def has_collided(self, other_obj):
        """
        Check if this object has collided with another circular object.

        Args:
            other_obj (CircleShape): The other object to check collision with.

        Returns:
            bool: True if the objects are overlapping, False otherwise.
        """

        if (
            self.position.distance_to(other_obj.position)
            <= (self.radius + other_obj.radius)
        ):
            return True

        return False

    def draw(self, screen):
        """
        Draw the object on the given Pygame screen. Intended for overrides in subclasses.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """
        pass

    def update(self, dt):
        """
        Update the object's state. Intended for overrides in subclasses

        Args:
            dt (float): Delta time since the last update.
        """
          
        pass
