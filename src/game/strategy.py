"""This module contains strategies used to play the game."""


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
