"""This module contains strategies used to play the game."""

import random

import pygame

from game import config


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

    _key_down_this_frame: bool = False

    def __init__(self) -> None:
        """Initialize this input strategy."""
        super().__init__()

    @classmethod
    def key_down(cls, val: bool):
        """Flag that the input key has or has not been pressed this frame."""
        cls._key_down_this_frame = val

    def get_move(self) -> bool:
        """Return whether or not to move the player."""
        return self._key_down_this_frame


class WordStrategy(Strategy):
    """Defines a strategy to move depending on word."""

    _current_word: str

    def __init__(self) -> None:
        """Initialize this word strategy."""
        super().__init__()
        self._current_word = ""
        self.new_word()

    def new_word(self) -> None:
        """Assign a new word for the strategy."""
        self._current_word = random.choice(config.WORDS).lower()
        print(self._current_word)

    def get_move(self) -> bool:
        """Return whether or not to move the player."""
        if pygame.key.get_pressed()[ord(self._current_word[0])]:
            self._current_word = self._current_word[1:]
            if not self._current_word:
                self.new_word()
            return True
        return False
