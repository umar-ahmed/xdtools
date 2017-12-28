"""
Contains the definition of Line.
"""

from point import Point
from artwork import Artwork


class Line(Artwork):
    """
    A Line.

    === Attributes ===
    name - The name of this Line as it appears in the Layers panel.
	uid - The unique id of this Line.
    position - The position of this Line.
    start - The starting Point of this Line.
    end - The ending Point of this Line.

	=== Operations ===
    """

    def __init__(self, uid, start_x, start_y, end_x, end_y, name='Line', x=0, y=0):
        """
        Instantiate a new Line.
        """
        self.uid = uid
        self.name = name
        self.position = Point(x, y)
        self.start = Point(start_x, start_y)
        self.end = Point(end_x, end_y)

    def __repr__(self):
        """
        Return a constructor-style representation of this Line.
        """
        return str.format(
            "Line(uid=\'{}\', name=\'{}\', position={}, start={}, end={})",
            self.uid, self.name, self.position, self.start, self.end)
