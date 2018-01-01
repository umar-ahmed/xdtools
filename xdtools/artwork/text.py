"""
Contains the definition of Text.
"""

from xdtools.utils import Point
from xdtools.artwork import Artwork


class Text(Artwork):
    """
    A Text element.

    === Attributes ===
    name - The name of this Text as it appears in the Layers panel.
	uid - The unique id of this Text.
	position - The position of this Text.

	=== Operations ===
    """

    def __init__(self, uid, raw_text, name='Text', x=0, y=0):
        """Instantiate a new Text object."""
        super().__init__(uid, name)
        self.raw_text = raw_text
        self.position = Point(x, y)

    def __repr__(self):
        """Return a constructor-style representation of this Text."""
        return str.format(
            "Text(uid=\'{}\', name=\'{}\', raw_text=\'{}\', position={}, styles={})",
            self.uid, self.name, self.raw_text, self.position, self.styles)
