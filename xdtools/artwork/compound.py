"""
Contains the definition of Compound.
"""

from xdtools.artwork import Artwork
from xdtools.utils import Point


class Compound(Artwork):
    """
    A compound shape.

    === Attributes ===
    uid - the unique id of this Compound shape.
    name - the name of this Compound shape as it appears in the Layers panel.
    position - the position of this Compound shape.
    path - the path of this Compound shape.
    children - the children contained in this Compound shape.
    operation - the operation performed on the paths of this Compound shape.

    === Operations ===
    """

    def __init__(self, uid: int, path: str, operation: str, children=None,
                 name='Compound', x=0, y=0) -> None:
        """Instantiate a new Compound."""
        super().__init__(uid, name)
        self.path = path
        self.operation = operation
        self.children = [] if children is None else children
        self.position = Point(x, y)

    def __repr__(self) -> str:
        """Return a constructor-style representation of this Compound."""
        children_str = [repr(child) for child in self.children]
        return str.format(
            "Compound(uid=\'{}\', path=\'{}\', operation=\'{}\', " +
            "children=[{}], name=\'{}\', position={})",
            self.uid, self.path, self.operation, children_str, self.name,
            self.position)
