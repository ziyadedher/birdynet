"""This module contains an I/O interface to the game."""

from typing import Tuple

from game import config
from game.player import Player
from game.world import World


class Game:
    """Manages the game and game state.

    Provides an interface with interaction with the game.
    """

    _player: Player
    _world: World

    def __init__(self) -> None:
        """Initialize this game with the optional given strategy <strat>."""
        self._player = Player()
        self._world = World()

    @property
    def size(self) -> Tuple[int, int]:
        """Get the size of the game."""
        return config.SIZE

    @property
    def player(self) -> Player:
        """Get the current player of this game."""
        return self._player

    @property
    def world(self) -> World:
        """Get the current world of this game."""
        return self._world

    def run(self) -> None:
        """Begin the update loop of this game and run until terminated."""
        while True:
            self.update()

    def update(self, delta_time: float = 0.001) -> None:
        """Update the game based off the given <delta_time>."""
        self._player.update(delta_time)
        self._world.update(delta_time)
