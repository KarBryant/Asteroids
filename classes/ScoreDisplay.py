import pygame


class ScoreDisplay:

    def __init__(self, font_size: int, position: tuple, color=(255, 255, 255)):
        """
         A class to display the player's score on the Pygame screen.

        Attributes:
            font_size (int): Size of the font to render the score.
            position (tuple): (x, y) coordinates on the screen where the score will be displayed.
            color (tuple): RGB color tuple for the text color. Defaults to white (255, 255, 255).
            font (pygame.font.Font): Pygame font object used to render the text.
        """

        self.color = color
        self.font_size = font_size
        self.position = position
        self.font = pygame.font.SysFont(None, font_size)

    def render(self, screen, score_variable):
        """
        Render the current score on the given Pygame screen.

        Args:
            screen (pygame.Surface): The Pygame surface to draw the score on.
            score_variable (int or str): The score value to display.

        Returns:
            pygame.Rect: The rectangle area of the rendered text on the screen.
        """
        self.text = self.font.render(f"Score: {score_variable}", True, self.color)
        return screen.blit(self.text, (self.position[0], self.position[1]))
