"""
Contains the definition of ColorFill.
"""

from xdtools.utils import Color
from .fill import Fill


class ColorFill(Fill):
    """Represents a ColorFill Style."""

    def __init__(self, r, g, b):
        """Instantiates this ColorFill."""
        super().__init__()
        self.color = Color(r, g, b)

    def __repr__(self):
        """Return a constructor-style representation of this ColorFill."""
        return str.format('ColorFill(color={})', repr(self.color))
