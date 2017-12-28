"""
Contains the definition of Point.
"""

from math import sqrt

class Point:
    """
    A point in a 2-dimensional coordinate system.

    ===Attributes===
    x - The horizontal component of this Point.
    y - The vertical component of this Point.
    """

    def __init__(self, x=0, y=0) -> None:
        """
        Instantiate a new Point.

        >>> p = Point(2, 3)
        >>> p.x
        2
        >>> p.y
        3
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Return a constructor-style representation of this Point.

        >>> p = Point(1, 2)
        >>> repr(p)
        Point(x=1, y=2)
        """
        return str.format("Point(x={}, y={})", self.x, self.y)

    def __eq__(self, other):
        """
        Return true iff other is equivalent to this Point.

        >>> p1 = Point(1, 2)
        >>> p2 = Point(1, 2)
        >>> p1 == p2
        True
        >>> p3 = Point(2, 4)
        >>> p1 == p3
        False
        """
        return (isinstance(other, Point)
                and other.x == self.x and other.y == self.y)

    def distance_from_point(self, other) -> float:
        """
        Returns the Euclidean distance between this Point and other.

        >>> p1 = Point(1, 2)
        >>> p2 = Point(1, 4)
        >>> p1.distance_from_point(p2)
        2.0
        """
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance_from_origin(self) -> float:
        """
        Returns the Euclidean distance between this Point and (0,0).

        >>> p = Point(3, 4)
        >>> p.distance_from_origin()
        5.0
        """
        return self.distance_from_point(Point(0, 0))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
