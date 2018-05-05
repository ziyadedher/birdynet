"""This module manages the main character of the game.
"""

from typing import Tuple

from game import config
from game.utils import Vector


class Player:
    """Manages a player and all respective information and actions such as
    movement, scoring, and death checking.
    """
    _position: Vector
    _velocity: Vector

    def __init__(self) -> None:
        """Initialize a player with no velocity and position defined in config.
        """
        self._position = Vector(*config.STARTING_COORDINATES)
        self._velocity = Vector.zero

    @property
    def radius(self) -> int:
        """Get the radius of this player.
        """
        return config.PLAYER_RADIUS

    @property
    def position(self) -> Tuple[float, float]:
        """Get the position of this player.
        """
        return self._position.coords

    # TODO: implement
