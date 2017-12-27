"""
Contains the definition of Artboard.
"""

from point import Point

class Artboard:
    """
    Represents an Artboard in an XD Project.

    ===Attributes===
    uid - The unique id of this Artbaord.
    name - The name of this Artboard as it appears in the Layers panel.
    width - The width of this Artboard.
    height - The height of this Artboard.
    position - The position of this Artboard.
    viewport_height - The height of the viewport in Preview mode.
    artworks - The artworks contained in this Artboard.

    === Operations ===
    """

    def __init__(self, uid, name, width=None, height=None, position=None, viewport_height=None, artworks=None):
        """Instantiate this Artboard."""
        self.uid = uid
        self.name = name
        self.width = width
        self.height = height
        self.position = Point(0, 0) if position is None else position
        self.viewport_height = viewport_height
        self.artworks = [] if artworks is None else artworks

    def __str__(self):
        """Return a string representation of this Artboard."""
        artwork_str = ','.join([str(artwork) for artwork in self.artworks])
        return str.format(
            "Artboard(uid=\'{}\', name=\'{}\', width={}, height={}, " +
            "position={}, viewport_height={}, artwork=[{}]",
            self.uid, self.name, self.width, self.height,
            self.position, self.viewport_height, artwork_str)
