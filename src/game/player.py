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

    deaths: int
    is_alive: bool
    is_colliding: bool

    def __init__(self) -> None:
        """Initialize a player with the optional given strategy <strat>.

        Gives no velocity and position defined in the configuration.
        """
        self._position = Vector(*config.STARTING_COORDINATES)
        self._velocity = Vector.zero()
        self._strat = IdleStrategy()

        self.deaths = 0
        self.is_alive = True
        self.is_colliding = False

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
    def velocity(self) -> Tuple[float, float]:
        """Get the velocity of this player."""
        return self._velocity.duplicate()

    def _update_velocity(self, delta_velocity: Vector) -> None:
        """Update player velocity by the given <delta_velocity>."""
        self._velocity += delta_velocity
        self._velocity = self._velocity.bound_magnitude(
            config.PLAYER_MAX_SPEED)

    def _update_position(self, delta_position: Vector) -> None:
        """Update player position by the given <delta_position>."""
        self._position += delta_position
        if self._position.y > config.HEIGHT - config.PLAYER_RADIUS:
            self.deaths += 1
            self.is_alive = False

    def kill(self) -> None:
        """Kill this player."""
        self.deaths += 1
        print("You died a total of " + str(self.deaths) + " times.")

    def jump(self) -> None:
        """Give the player an upward impulse to jump."""
        if self._position.y < config.PLAYER_RADIUS:
            return
        self._velocity = Vector(self._velocity.x, 0)
        self._update_velocity(Vector(0, -config.PLAYER_JUMP))

    def update(self, delta_time: float) -> None:
        """Update the player based off the given <delta_time>."""
        self._update_velocity(Vector(0, config.GRAVITY * delta_time))

        if self._strat.get_move():
            self.jump()

        self._update_position(self._velocity * delta_time)
