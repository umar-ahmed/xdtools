"""
Contains the definition of Stroke.
"""

from .style import Style


class Stroke(Style):
    """
    Represents a stroke Style.

    ===Attributes===
    width - The width of this Stroke style.
    align - The alignment of the stroke ('inside', 'outside', 'center')

    ===Operations===
    """

    def __init__(self, width, align):
        super().__init__('stroke')
        self.width = width
        self.align = align
