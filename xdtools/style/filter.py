"""
Contains the definition of Filter.
"""

from .style import Style


class Filter(Style):
    """Represents a Filter Style."""

    def __init__(self):
        super().__init__('filter')
