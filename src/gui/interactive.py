"""This module contains a GUI to the game and manages user input.
"""

import sys
import pygame
from pygame import gfxdraw

from gui import config
from game.game import Game


class InteractiveGUI:
    """Manages an interactive GUI for the user, controlling both
    display and input.
    """
    game: Game
    surface: pygame.Surface
    clock: pygame.time.Clock

    def __init__(self, game: Game) -> None:
        """Initialize the interactive gui.
        """
        self.game = Game()

        pygame.init()
        self.surface = pygame.display.set_mode(game.size)
        pygame.display.set_caption(config.WINDOW_CAPTION)

        self.clock = pygame.time.Clock()

    def run(self) -> None:
        """Begin execution of the game and GUI and run until terminated.
        """
        while True:
            self.refresh()

    def refresh(self) -> None:
        """Refresh the display to redraw everything.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.surface.fill(config.BACKGROUND_COLOR)
        self._draw_all()
        pygame.display.flip()

    def _draw_all(self) -> None:
        """Draw all elements of the game.
        """
        self._draw_world()
        self._draw_player()

    def _draw_world(self) -> None:
        """Draw the world.
        """
        # TODO: implement

    def _draw_player(self) -> None:
        """Draw the player.
        """
        params = (self.surface,
                  *self.game.player.position, self.game.player.radius,
                  config.PLAYER_COLOR)
        gfxdraw.aacircle(*params)
        gfxdraw.filled_circle(*params)
