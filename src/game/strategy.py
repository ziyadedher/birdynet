"""This module contains strategies used to play the game."""

import pygame
import time


class Strategy:
    """Defines an abstract strategy that can be built on."""

    def __init__(self) -> None:
        """Initialize this abstract strategy.

        Do not initialize an abstract strategy.
        """
        pass

    def get_move(self) -> bool:
        """Return whether or not to move the player."""
        raise NotImplementedError


class IdleStrategy(Strategy):
    """Defines a strategy to do nothing at all."""

    def __init__(self) -> None:
        """Initialize this idle strategy."""
        super().__init__()

    def get_move(self) -> bool:
        """Return whether or not to move the player."""
        return False


class InputStrategy(Strategy):
    """Defines a strategy to move when the user hits space."""

    REPEAT_TIME: float = 0.1

    def __init__(self) -> None:
        """Initialize this input strategy."""
        self._last_input_time = 0
        super().__init__()

    def get_move(self) -> bool:
        """Return whether or not to move the player."""
        allowed = time.time() - self._last_input_time >= self.REPEAT_TIME
        if allowed and pygame.key.get_pressed()[pygame.K_SPACE]:
            self._last_input_time = time.time()
            return True
        return False
