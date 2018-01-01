"""
Contains the definition of Opacity.
"""

from .style import Style


class Opacity(Style):
    """
    Represents a Opacity Style.

    ===Attributes===
    amount - the amount of opacity.

    ===Operations===
    """

    def __init__(self, amount):
        super().__init__('opacity')
        self.amount = amount

    def __repr__(self):
        """Return a constructor-style representation of this Opacity."""
        return str.format('Opacity(amount={})', repr(self.amount))
