"""This module provides a user entry point into the game.
"""

from game.game import Game
from gui.interactive import InteractiveGUI


if __name__ == '__main__':
    GAME = Game()
    GUI = InteractiveGUI(GAME)

    GUI.run()
