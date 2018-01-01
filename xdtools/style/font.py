"""
Contains the definition of Font.
"""

from .style import Style

class Font(Style):
    """
    Represents a font style.
    """

    def __init__(self, family, style, size, postscript_name):
        """Initialize this Font."""
        super().__init__('font')
        self.family = family
        self.style = style
        self.size = size
        self.postscript_name = postscript_name

    def __repr__(self):
        """Return a constructor-style representation of this Font."""
        return str.format(
            'Font(family=\'{}\', style=\'{}\', size={}, postscript_name=\'{}\')',
            repr(self.family), repr(self.style), repr(self.size), repr(self.postscript_name))
