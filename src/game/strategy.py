"""This module contains strategies used to play the game.
"""


class Strategy:
    """Defines an abstract strategy that can be built on.
    """

    def __init__(self) -> None:
        """Initialize this abstract strategy.

        Do not initialize an abstract strategy.
        """
        pass

    # TODO: implement


class IdleStrategy(Strategy):
    """Defines a strategy to do nothing at all.
    """

    def __init__(self) -> None:
        """Initialize this idle strategy.
        """
        super().__init__()

    # TODO: implement
