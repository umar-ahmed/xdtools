"""
Contains the definition of ClipPath.
"""

class ClipPath(object):
    """Represents a clip path."""
    def __init__(self, uid, type_, children=None):
        """Initialize this ClipPath."""
        self.uid = uid
        self.type = type_
        self.children = children if children is not None else []

    def __repr__(self):
        """Return a constructor-style representation of this ClipPath."""
        return str.format('ClipPath(uid={}, type={}, children={})',
                          repr(self.uid), repr(self.type), repr(self.children))
