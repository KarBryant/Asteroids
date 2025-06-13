from .shot import Shot
from .circleshape import CircleShape
import pygame
import constants


class Player(CircleShape):
    """
    Represents the player-controlled spaceship in the game.

    The player can rotate, move, and shoot projectiles.
    """

    def __init__(self, x, y):
        """
        Initialize the player at a given position with default stats.

        Args:
            x (float): Initial x-coordinate of the player.
            y (float): Initial y-coordinate of the player.
        """

        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.position = pygame.Vector2(x, y)
        self.shot_cooldown = 0


    def triangle(self):
        """
        Calculate the vertices of the player's triangle-shaped ship.

        Returns:
            list[pygame.Vector2]: List of 3 vertices defining the ship's triangle.
        """

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Draw the player as a triangle on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on.
        """

        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta_time):
        """
        Rotate the player based on delta time.

        Args:
            delta_time (float): Time since the last frame/update.
        """

        self.rotation += constants.PLAYER_TURN_SPEED / delta_time

    def update(self, delta_time):
        """
        Handle user input to update the player's state.

        Args:
            delta_time (float): Time since the last update/frame.
        """

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_SPACE]:
            self.shoot(delta_time)

    def move(self, delta_time):
        """
        Move the player forward or backward depending on input. If the player goes out of screen bounds, they will be
        wrapped to the opposite screen edge.

        Args:
            delta_time (float): Time since the last update/frame.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * (delta_time / 10)

        if self.position[0] < 0:
            self.position = pygame.math.Vector2(constants.SCREEN_WIDTH, self.position[1])
        if self.position[0] > constants.SCREEN_WIDTH:
            self.position = pygame.math.Vector2(0, self.position[1])
        if self.position[1] < 0:
            self.position = pygame.math.Vector2(self.position[0], constants.SCREEN_HEIGHT)
        if self.position[1] > constants.SCREEN_HEIGHT:
            self.position = pygame.math.Vector2(self.position[0], 0)
        


    def shoot(self, delta_time):
        """
        Fire a projectile if the cooldown allows it.

        Args:
            delta_time (float): Time since the last update/frame.
        """
        
        self.shot_cooldown += delta_time / 3000
        if self.shot_cooldown > constants.PLAYER_SHOOT_COOLDOWN:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
            shot.velocity += forward / constants.PLAYER_SHOOT_DRAG
            self.shot_cooldown = 0
