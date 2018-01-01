"""
Contains the definition of PatternFill.
"""

from .fill import Fill

class PatternFill(Fill):
    """
    Represents an image fill style.
    """

    def __init__(self, width, height, scale_behavior, image_href):
        """Instantiates this PatternFill."""
        super().__init__()
        self.width = width
        self.height = height
        self.scale_behavior = scale_behavior
        self.image_href = image_href

    def __repr__(self):
        """Return a constructor-style representation of this PatternFill."""
        return str.format(
            'PatternFill(width={}, height={}, scale_behavior={}, image_href={})',
            repr(self.width), repr(self.height), repr(self.scale_behavior),
            repr(self.image_href))
