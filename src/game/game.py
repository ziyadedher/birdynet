"""This module contains an I/O interface to the game.
"""

from typing import Optional

import time

from player import Player
from world import World
from strategy import Strategy, IdleStrategy


class Game:
    """Manages the game and game state.

    Provides an interface with interaction with the game.
    """
    _player: Player
    _world: World

    def __init__(self, strat: Optional[Strategy] = None) -> None:
        """Initialize this game with the optional given strategy <strat>.
        """
        self._player = Player()
        self._world = World()
        self.attach_strategy(strat)

    @property
    def player(self) -> Player:
        """Get the current player of this game.
        """
        return self._player

    @property
    def world(self) -> World:
        """Get the current world of this game.
        """
        return self._world

    def attach_strategy(self, strat: Strategy) -> None:
        """Attache the given strategy to the game to control the player.
        """
        self._strat = strat if strat else IdleStrategy()

    def begin(self) -> None:
        """Begin the update loop of this game and run until terminated.
        """
        past_time = time.time()
        while True:
            delta_time = time.time() - past_time
            past_time += delta_time

            self._update(delta_time)

    def _update(self, delta_time: float) -> None:
        """Update the game based off the given <delta_time>.
        """
        # TODO: implement
        pass
