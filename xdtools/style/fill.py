"""
Contains the definition of Fill.
"""

from .style import Style

class Fill(Style):
    """Represents a fill Style."""

    def __init__(self):
        super().__init__('fill')
