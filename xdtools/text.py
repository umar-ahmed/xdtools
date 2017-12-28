"""
Contains the definition of Text.
"""

from point import Point
from artwork import Artwork

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
        self.uid = uid
        self.raw_text = raw_text
        self.name = name
        self.position = Point(x, y)

    def __repr__(self):
        """Return a constructor-style representation of this Text."""
        return str.format(
            "Text(uid=\'{}\', name=\'{}\', raw_text=\'{}\', position={})",
            self.uid, self.name, self.raw_text, self.position)
