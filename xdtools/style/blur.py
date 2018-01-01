"""
Contains the definition of Blur.
"""

from .filter import Filter


class Blur(Filter):
    """
    Represents a blur filter.
    """

    def __init__(self, amount, brightness, fill_opacity, background_effect):
        """Initialize this Blur."""
        super().__init__()
        self.amount = amount
        self.brightness = brightness
        self.fill_opacity = fill_opacity
        self.background_effect = background_effect

    def __repr__(self):
        """Return a constructor-style representation of this Blur."""
        return str.format(
            'Blur(amount={}, brightness={}, fill_opacity={}, background_effect={}',
            repr(self.amount), repr(self.brightness), repr(self.fill_opacity),
            repr(self.background_effect))
