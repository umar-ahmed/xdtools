"""
Contains the definition of Group.
"""

from xdtools.utils.point import Point
from xdtools.artwork.artwork import Artwork


class Group(Artwork):
    """
    A Group.

    === Attributes ===
    uid - The unique id of this Group.
    name - The name of this Group as it appears in the Layers panel.
    position - the position of this Group.
    children - the children of this Group.

    === Operations ===
    """

    def __init__(self, uid, name='Group', x=0, y=0, children=None):
        """Instantiate a new Group."""
        self.uid = uid
        self.name = name
        self.position = Point(x, y)
        self.children = [] if children is None else children

    def __repr__(self):
        """Return a constructor-style representation of this Group."""
        children_str = ','.join([str(child) for child in self.children])
        return str.format(
            "Group(uid=\'{}\', name=\'{}\', position={}, children=[{}])",
            self.uid, self.name, self.position, children_str)

    def add_child(self, child) -> None:
        """Add child to this Group's children."""
        self.children.append(child)
