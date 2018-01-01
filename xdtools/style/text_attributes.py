"""
Contains the definition of TextAttributes.
"""

from .style import Style


class TextAttributes(Style):
    """Represents a TextAttributes Style."""

    def __init__(self, letter_spacing, paragraph_align):
        """Initialize this TextAttributes."""
        super().__init__('textAttributes')
        self.letter_spacing = letter_spacing
        self.paragraph_align = paragraph_align

    def __repr__(self):
        """Return a constructor-style representation of this TextAttributes."""
        return str.format(
            'TextAttributes(letter_spacing={}, paragraph_align={})',
            repr(self.letter_spacing), repr(self.paragraph_align))
