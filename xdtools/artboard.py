"""
Contains the definition of Artboard.
"""

from xdtools.utils.point import Point


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
    artwork - The artwork contained in this Artboard.

    === Operations ===
    """

    def __init__(self, uid, name, width=None, height=None, position=None,
                 viewport_height=None, artwork=None):
        """Instantiate this Artboard."""
        self.uid = uid
        self.name = name
        self.width = width
        self.height = height
        self.position = Point(0, 0) if position is None else position
        self.viewport_height = viewport_height
        self.artwork = [] if artwork is None else artwork

    def __repr__(self):
        """Return a constructor-style representation of this Artboard."""
        artwork_str = ','.join([str(artwork) for artwork in self.artwork])
        return str.format(
            "Artboard(uid=\'{}\', name=\'{}\', width={}, height={}, " +
            "position={}, viewport_height={}, artwork=[{}]",
            self.uid, self.name, self.width, self.height,
            self.position, self.viewport_height, artwork_str)
