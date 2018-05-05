"""This module contains and manages a game world."""

from typing import List, Tuple

import random

from game import config


class Wall:
    """Represents a wall barrier in the game."""

    gap_start: int
    location: float

    def __init__(self, gap_start: int) -> None:
        """Initialize a wall with the given <gap_start>.

        The gap start is the height of the bottom of the gap
        from the top of the game.
        """
        self.gap_start = gap_start
        self.location = config.WIDTH


class World:
    """Manages a world including updating and generating the terrain."""

    _walls: List[Wall]

    def __init__(self) -> None:
        """Initialize a world."""
        self._walls = [Wall((config.HEIGHT - config.WALL_GAP_HEIGHT) // 2)]

    def get_wall_information(self) -> List[Tuple[float, int]]:
        """Get information about all walls in the world."""
        return [(wall.location, wall.gap_start) for wall in self._walls]

    @property
    def ground_height(self) -> int:
        """Get the height of the ground from the bottom of the game."""
        return config.GROUND_HEIGHT

    @property
    def wall_width(self) -> int:
        """Get the width of the walls."""
        return config.WALL_WIDTH

    @property
    def wall_gap_height(self) -> int:
        """Get the height of the gap of the walls."""
        return config.WALL_GAP_HEIGHT

    def update(self, delta_time: float) -> None:
        """Update the world based off the given <delta_time>."""
        if self._walls[0].location < -config.WALL_WIDTH:
            self._walls.pop(0)

        # FIXME
        if self._walls[-1].location < config.WIDTH - config.WALL_SPACING:
            gap = random.randint(config.WALL_GAP_PADDING,
                                 config.HEIGHT - config.WALL_GAP_HEIGHT
                                 - config.WALL_GAP_PADDING)
            self._walls.append(Wall(gap))

        for wall in self._walls:
            wall.location -= config.WALL_SPEED * delta_time
