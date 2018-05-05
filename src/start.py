"""This module provides a user entry point into the game."""

from game.game import Game
from game.strategy import InputStrategy
from gui.interactive import InteractiveGUI


if __name__ == '__main__':
    GAME = Game()
    GAME.player.attach_strategy(InputStrategy())

    GUI = InteractiveGUI(GAME)

    GUI.run()
