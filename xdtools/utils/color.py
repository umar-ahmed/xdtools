"""
Contains the definition of Color.
"""

class Color:
    """
    Represents a color in an Adobe XD project.

    ===Attributes===
    r - The value of the red channel (0-255).
    g - The value of the blue channel (0-255).
    b - The value of the green channel (0-255).

    ===Operations===
    """

    def __init__(self, r=0, g=0, b=0):
        """
        Instantiate a new Color.

        >>> c = Color(50, 123, 255)
        >>> c.r
        50
        >>> c.g
        123
        >>> c.b
        255
        """
        self.r = self.__clamp_value(r)
        self.g = self.__clamp_value(g)
        self.b = self.__clamp_value(b)

    def __repr__(self):
        """Return a constructor-style representation of this Color."""
        return str.format('Color(r={}, g={}, b={})', self.r, self.g, self.b)

    def to_hex(self):
        """Return a string hexidecimal representation of this Color."""
        return '#%02x%02x%02x' % (self.r, self.g, self.b)

    def __clamp_value(self, value):
        """Clamp value to be in the range 0-255 (inclusive)."""
        return max(0, min(value, 255))
