"""
Contains the definition of DropShadow.
"""

from .filter import Filter

class DropShadow(Filter):
    """
    Represents a drop shadow filter.
    """

    def __init__(self, offset_x, offset_y, blur_radius, color):
        """Initialize this DropShadow."""
        super().__init__()
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.blur_radius = blur_radius
        self.color = color

    def __repr__(self):
        """Return a constructor-style representation of this DropShadow."""
        return str.format(
            'DropShadow(offset_x={}, offset_y={}, blur_radius={}, color={}',
            repr(self.offset_x), repr(self.offset_y), repr(self.blur_radius),
            repr(self.color))
