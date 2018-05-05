"""This module contains utilities that the rest of the game may use.
"""


class Vector:
    """Stores two-dimensional vector object used for location, velocity,
    and other coordinate-based values.
    """
    _x_coordinate: float
    _y_coordinate: float

    def __init__(self, x: float, y: float) -> None:
        """Initialize this vector with the given <x> and <y> values.
        """
        self._x_coordinate = x
        self._y_coordinate = y

    @classmethod
    @property
    def zero(cls) -> 'Vector':
        """Get a newly constructed zero vector.
        """
        return Vector(0.0, 0.0)

    @property
    def coords(self) -> float:
        """Get the coordinates of this vector.
        """
        return (self._x_coordinate, self._y_coordinate)
