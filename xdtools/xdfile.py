"""
Contains the definition of XDFile.
"""

class XDFile:
    """
    Represents an Adobe XD project file.

    ===Attributes===
    name - The name of the XD file.
    path - The absolute path to the XD file.
    thumbnail_path - The absolute path to the thumbnail file.
    preview_path - The absolute path to the preview file.
    color_swatches - The list of color swatches in this XDFile.
    artboards - The list of artboards in this XDFile.
    """

    def __init__(self, name, path, thumbnail_path, preview_path, color_swatches=None, artboards=None):
        """Initialize a new XDFile."""
        self.name = name
        self.path = path
        self.thumbnail_path = thumbnail_path
        self.preview_path = preview_path
        self.color_swatches = [] if color_swatches is None else color_swatches
        self.artboards = [] if artboards is None else artboards

