"""
Contains the definition of Ellipse.
"""

from xdtools.utils import Point
from xdtools.artwork import Artwork


class Ellipse(Artwork):
    """
    An ellipse.

    === Attributes ===
    uid - the unique id of this Ellipse.
    name - the name of this Ellipse as it appears in the Layers panel.
    position - the position of this Ellipse.
    width - the width of this Ellipse, in pixels.
    height - the height of this Ellipse, in pixels.

    === Operations ===
    """

    def __init__(self, uid, name='Ellipse', x=0, y=0, width=50, height=50):
        """Instantiate a new Ellipse."""
        super().__init__(uid, name)
        self.position = Point(x, y)
        self.width = width
        self.height = height

    def __repr__(self):
        """Return a constructor-style representation of this Ellipse."""
        return str.format(
            "Ellipse(uid=\'{}\', name=\'{}\', position={}, width={}, height={}, styles={})",
            self.uid, self.name, self.position, self.width, self.height, self.styles)
