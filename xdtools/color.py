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
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        """Return a constructor-style representation of this Color."""
        return str.format('Color(r={}, g={}, b={})', self.r, self.g, self.b)
