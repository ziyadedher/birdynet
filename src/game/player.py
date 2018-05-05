"""This module manages the main character of the game."""

from typing import Tuple

from game import config
from game.utils import Vector
from game.strategy import Strategy, IdleStrategy


class Player:
    """Manages a player and all respective information and actions.

    Such management includes movement, scoring, and death checking.
    """

    _position: Vector
    _velocity: Vector
    _strat: Strategy

    def __init__(self) -> None:
        """Initialize a player with the optional given strategy <strat>.

        Gives no velocity and position defined in the configuration.
        """
        self._position = Vector(*config.STARTING_COORDINATES)
        self._velocity = Vector.zero()
        self._strat = IdleStrategy()

    def attach_strategy(self, strat: Strategy) -> None:
        """Attach the given strategy to control the player."""
        self._strat = strat

    @property
    def radius(self) -> int:
        """Get the radius of this player."""
        return config.PLAYER_RADIUS

    @property
    def position(self) -> Tuple[float, float]:
        """Get the position of this player."""
        return self._position.duplicate()

    @property
    def is_alive(self) -> bool:
        """Get whether or not the player is still alive."""
        return self._position.y < config.HEIGHT - config.PLAYER_RADIUS

    # TODO: fix movement code
    def jump(self) -> None:
        """Give the player an upward impulse to jump."""
        x, y = self._velocity.x, self._velocity.y
        self._velocity = Vector(x, min(y + 500, config.PLAYER_MAX_SPEED))

    def update(self, delta_time: float) -> None:
        """Update the player based off the given <delta_time>."""
        x, y = self._velocity.x, self._velocity.y
        self._velocity = Vector(x, y - (config.GRAVITY * delta_time))

        if self._strat.get_move():
            self.jump()

        x, y = self._position.x, self._position.y
        self._position = Vector(x, y - (self._velocity.y * delta_time))
