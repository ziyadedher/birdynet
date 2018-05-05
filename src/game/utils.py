"""This module contains utilities that the rest of the game may use."""


class Vector:
    """Stores two-dimensional vector object.

    Can be used for location, velocity, and other coordinate-based values.
    """

    _x: float
    _y: float

    def __init__(self, x: float, y: float) -> None:
        """Initialize this vector with the given <x> and <y> values."""
        self._x = x
        self._y = y

    def duplicate(self) -> 'Vector':
        """Return a duplicate of this vector."""
        return Vector(self._x, self._y)

    @classmethod
    def zero(cls) -> 'Vector':
        """Get a newly constructed zero vector."""
        return Vector(0.0, 0.0)

    @property
    def x(self) -> float:
        """Get the x-coordinate of this vector."""
        return self._x

    @property
    def y(self) -> float:
        """Get the y-coordinate of this vector."""
        return self._y
