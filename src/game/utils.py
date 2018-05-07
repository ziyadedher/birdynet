"""This module contains utilities that the rest of the game may use."""

import math


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

    def __iadd__(self, other: 'Vector') -> 'Vector':
        """Override += operator to work for vector addition."""
        self._x += other.x
        self._y += other.y
        return self

    def __mul__(self, scalar: float) -> 'Vector':
        """Override * operator to work for scalar multiplication."""
        return Vector(self._x * scalar, self._y * scalar)

    def duplicate(self) -> 'Vector':
        """Return a duplicate of this vector."""
        return Vector(self._x, self._y)

    def normalize(self) -> 'Vector':
        """Return a normalized copy of this vector."""
        return self * (1 / self.magnitude)

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

    @property
    def magnitude(self) -> float:
        """Get the magnitude of this vector."""
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def bound_magnitude(self, bound: float) -> 'Vector':
        """Return a magnitude-bounded copy of this vector."""
        if self.magnitude > bound:
            return self.normalize() * bound
        return self.duplicate()
