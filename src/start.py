"""This module provides a user entry point into the game."""

from game import strategy
from game.game import Game
from gui.interactive import InteractiveGUI

if __name__ == '__main__':
    GAME = Game()
<<<<<<< HEAD
    GAME.player.attach_strategy(strategy.InputStrategy())
=======
    GAME.player.attach_strategy(strategy.InputStrategy)
>>>>>>> 475a65397e174cc1758430ac58f514384dd59706

    GUI = InteractiveGUI(GAME)

    GUI.run()
