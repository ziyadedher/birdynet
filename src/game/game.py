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
        while self._player.is_alive:
            self.update()

    def _detect_collisions(self) -> None:
        """Detect any collisions that may have happened."""
        # FIXME
        for location, gap_start in self._world.get_wall_information():
            x_between = (location - config.PLAYER_RADIUS <
                         self._player.position.x
                         < location + config.PLAYER_RADIUS + config.WALL_WIDTH)
            if x_between:
                y_between = (gap_start + config.PLAYER_RADIUS <
                             self._player.position.y
                             < gap_start
                             - config.PLAYER_RADIUS + config.WALL_GAP_HEIGHT)
                if not y_between:
                    if not self._player.is_colliding:
                        self._player.is_colliding = True
                        self._player.kill()
                    return
        self._player.is_colliding = False

    def update(self, delta_time: float = 0.001) -> None:
        """Update the game based off the given <delta_time>."""
        self._player.update(delta_time)
        self._world.update(delta_time)
        self._detect_collisions()
