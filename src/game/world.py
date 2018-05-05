"""This module contains and manages a game world.
"""

from typing import List

from game import config


class Wall:
    """Represents a wall barrier in the game.
    """

    def __init__(self, gap_center_height: int) -> None:
        """Initialize a wall with the given <gap_center_height> which
        is the height of the center of the gap from the bottom of the game.
        """
        pass

    # TODO: implement


class World:
    """Manages a world including updating and generating the terrain.
    """
    _walls: List[Wall]

    def __init__(self) -> None:
        """Initialize a world.
        """
        pass

    @property
    def ground_height(self) -> int:
        """Get the height of the ground from the bottom of the game.
        """
        return config.GROUND_HEIGHT

    # TODO: implement
