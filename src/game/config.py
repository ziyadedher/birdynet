"""This module contains static configuration for all aspects of the game."""

from typing import Tuple


# Game configuration
WIDTH: int = 800
HEIGHT: int = 800
SIZE: Tuple[int, int] = (WIDTH, HEIGHT)

# World configuration
GRAVITY: float = 750
GROUND_HEIGHT: int = 50
WALL_WIDTH: int = 25

# Player configuration
PLAYER_MAX_SPEED: int = 750
PLAYER_JUMP: int = 400
PLAYER_RADIUS: int = 15
RIGHT_OFFSET: int = 100
STARTING_COORDINATES: Tuple[int, int] = (RIGHT_OFFSET, HEIGHT // 2)
