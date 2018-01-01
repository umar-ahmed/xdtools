"""
Contains the definitions of Gradient and GradientStop.
"""

from xdtools.utils import Color


class Gradient:
    """
    Represents a gradient.

    ===Attributes===
    uid - The unique id of this Gradient.
    type - The type of this Gradient.
    stops - The list of stops in this Gradient.

    ===Operations===
    """

    def __init__(self, uid, type_, stops=None):
        """Initialize this Gradient with a uid and (optionally) a list of stops."""
        self.uid = uid
        self.type = type_
        self.stops = stops if stops is not None else []

    def __repr__(self):
        """Return a constructor-style representation of this Gradient."""
        return str.format("Gradient(uid={}, type={} stops={})",
                          repr(self.uid), repr(self.type), repr(self.stops))


class GradientStop:
    """Represents a stop in a GradientFill"""

    def __init__(self, offset, r=0, g=0, b=0):
        """Initialize this GradientStop."""
        self.offset = offset
        self.color = Color(r, g, b)

    def __repr__(self):
        """Return a constructor-style representation of this GradientStop."""
        return str.format('GradientStop(offset={}, color={}',
                          repr(self.offset), repr(self.color))
