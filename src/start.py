"""This module provides a user entry point into the game."""

from game.game import Game
from game.strategy import InputStrategy, WordStrategy
from gui.interactive import InteractiveGUI


if __name__ == '__main__':
    GAME = Game()
    GAME.player.attach_strategy(WordStrategy())

    GUI = InteractiveGUI(GAME)

    GUI.run()
