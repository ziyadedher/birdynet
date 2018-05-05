"""This module contains static configuration for all aspects of the game."""

from typing import Tuple

# Words
word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

# Game configuration
WIDTH: int = 800
HEIGHT: int = 800
SIZE: Tuple[int, int] = (WIDTH, HEIGHT)

# World configuration
GRAVITY: float = 2250
GROUND_HEIGHT: int = 50

# Wall configuration
WALL_SPEED: int = 250
WALL_WIDTH: int = 75
WALL_GAP_HEIGHT: int = 150
WALL_GAP_PADDING: int = 50
WALL_SPACING: int = 500

# Player configuration
PLAYER_MAX_SPEED: int = 1000
PLAYER_JUMP: int = 625
PLAYER_RADIUS: int = 15
RIGHT_OFFSET: int = 100
STARTING_COORDINATES: Tuple[int, int] = (RIGHT_OFFSET, HEIGHT // 2)
