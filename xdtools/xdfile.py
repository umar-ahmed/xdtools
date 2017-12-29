"""
Contains the definition of XDFile.
"""

from zipfile import ZipFile
import json
from xdtools.utils import Color
from xdtools.utils import parse_artboard


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

    def __init__(self, path, mode='r'):
        """Open the XD file with mode read 'r' or  write 'w'."""
        if mode not in ['r', 'w']:
            raise ValueError("XDFile requires mode 'r' or 'w'")

        self._name = None
        self._path = path
        self._thumbnail_path = None
        self._preview_path = None
        self._color_swatches = None
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
            manifest_file_json = self.__get_manifest_file_json()
            self._name = manifest_file_json['name']
        return self._name

    @property
    def thumbnail_path(self):
        if self._thumbnail_path is None:
            manifest_file_json = self.__get_manifest_file_json()
            self._thumbnail_path = manifest_file_json['components'][0]['path']
        return self._thumbnail_path

    @property
    def preview_path(self):
        if self._preview_path is None:
            manifest_file_json = self.__get_manifest_file_json()
            self._preview_path = manifest_file_json['components'][0]['path']
        return self._preview_path

    @property
    def color_swatches(self):
        if self._color_swatches is None:
            resources_file_json = self.__get_resources_file_json()
            color_swatches_node = resources_file_json['resources']['meta']['ux']['colorSwatches']
            color_swatches = []
            for node in color_swatches_node:
                value = node['value']
                color = Color(value['r'], value['g'], value['b'])
                color_swatches.append(color)
            self._color_swatches = color_swatches
        return self._color_swatches

    @property
    def artboards(self):
        if self._artboards is None:
            artboards = []
            manifest_file_json = self.__get_manifest_file_json()
            artboard_nodes = manifest_file_json['children'][0]['children']
            for artboard_node in artboard_nodes:
                artboard = parse_artboard(artboard_node, self._file)
                artboards.append(artboard)
            self._artboards = artboards
        return self._artboards

    def __get_resources_file_json(self):
        # """Return the resources JSON file of this XD File"""
        if self._file is not None:
            resources_file = self._file.read(
                "resources/graphics/graphicContent.agc")
            return json.loads(resources_file)
        else:
            raise Exception()

    def __get_manifest_file_json(self):
        # """Return the manifest JSON file of this XD File"""
        if self._file is not None:
            manifest_file = self._file.read("manifest")
            return json.loads(manifest_file)
        else:
            raise Exception()
