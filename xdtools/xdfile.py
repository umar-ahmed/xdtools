"""
Contains the definition of XDFile.
"""

from zipfile import ZipFile
from xdtools.utils import *


class XDFile:
    """
    Represents an Adobe XD project file.

    ===Attributes===
    name - The name of the XD file.
    path - The absolute path to the XD file.
    thumbnail_path - The absolute path to the thumbnail file.
    preview_path - The absolute path to the preview file.
    color_swatches - The list of color swatches in this XDFile.
    gradients - The list of gradients in this XDFile.
    artboards - The list of artboards in this XDFile.
    """

    def __init__(self, path, mode='r'):
        """Open the XD file with mode read 'r' or  write 'w'."""
        if mode not in ['r', 'w']:
            raise ValueError("XDFile requires mode 'r' or 'w'")

        self._name = None
        self._path = path
        self._thumbnail_path = None
        self._preview_path = None
        self._color_swatches = None
        self._gradients = None
        self._artboards = None

        if mode == 'r':
            self._file = ZipFile(path, 'r')
        elif mode == 'w':
            raise NotImplementedError('Writing to XD files is not supported yet!')

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        self.close()

    def close(self):
        """Closes this XDFile."""
        self._file.close()

    @property
    def name(self):
        if self._name is None:
            self._name = parse_name(self._file)
        return self._name

    @property
    def thumbnail_path(self):
        if self._thumbnail_path is None:
            self._thumbnail_path = parse_thumbnail_path(self._file)
        return self._thumbnail_path

    @property
    def preview_path(self):
        if self._preview_path is None:
            self._preview_path = parse_preview_path(self._file)
        return self._preview_path

    @property
    def color_swatches(self):
        if self._color_swatches is None:
            self._color_swatches = parse_color_swatches(self._file)
        return self._color_swatches

    @property
    def gradients(self):
        if self._gradients is None:
            self._gradients = parse_gradients(self._file)
        return self._gradients

    @property
    def artboards(self):
        if self._artboards is None:
            self._artboards = parse_artboards(self._file)
        return self._artboards
