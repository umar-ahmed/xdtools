"""
Contains the definitions of various exceptions related to parsing XD files.
"""

class XDToolsException(Exception):
    """Base exception for xdtools."""


class UnknownArtworkException(XDToolsException):
    """Represents an exception where the type of artwork is unknown."""
    pass


class UnknownShapeException(UnknownArtworkException):
    """Represents an exception where the type of shape is unknown."""
    pass


class UnknownStyleException(XDToolsException):
    """Represents an exception where type of style is unknown."""
    pass


class DuplicateStyleTypeException(XDToolsException):
    """
    Represents an Exception resulting from duplicate style types in the same
    artwork.
    """
    pass

class UnknownFillTypeException(UnknownStyleException):
    """Represents an exception where the type of fill is unknown"""
    pass


class UnknownStrokeTypeException(UnknownStyleException):
    """Represents an exception where the type of stroke is unknown"""
    pass


class UnknownFilterTypeException(UnknownStyleException):
    """Represents an exception where the type of filter is unknown"""
    pass
