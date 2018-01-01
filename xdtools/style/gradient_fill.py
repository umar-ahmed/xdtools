"""
Contains the definition of GradientFill.
"""

from xdtools.utils import Color
from .fill import Fill


class GradientFill(Fill):
    """Represents a GradientFill Style."""

    def __init__(self, start, end, gradient):
        """Instantiates this GradientFill."""
        super().__init__()
        self.start = start
        self.end = end
        self.gradient = gradient

    def __repr__(self):
        """Return a constructor-style representation of this GradientFill."""
        return str.format('GradientFill(start={}, end={}, gradient={})',
                          repr(self.start), repr(self.end), repr(self.gradient))
