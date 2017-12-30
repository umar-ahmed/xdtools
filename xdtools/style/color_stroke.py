"""
Contains the definition of ColorStroke.
"""

from xdtools.utils import Color
from .stroke import Stroke


class ColorStroke(Stroke):
    """Represents a ColorStroke Style."""

    def __init__(self, width, align, r, g, b):
        """Instantiates this ColorStroke."""
        super().__init__(width, align)
        self.color = Color(r, g, b)

    def __repr__(self):
        """Return a constructor-style representation of this ColorStroke."""
        return str.format('ColorStroke(width={}, align={}, color={})',
                          repr(self.width), repr(self.align), repr(self.color))
