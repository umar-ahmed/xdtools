"""
File parser.
"""

import zipfile
import json
import argparse
import os

from xdfile import XDFile
from artboard import Artboard
from point import Point
from ellipse import Ellipse
from rectangle import Rectangle
from line import Line
from text import Text
from path import Path
from group import Group
from compound import Compound
from color import Color


class UnknownArtworkException(Exception):
    """Represents an exception where the type of shape is unknown."""
    pass


class UnknownShapeException(UnknownArtworkException):
    """Represents an exception where the type of shape is unknown."""
    pass


def extract_artwork(node):
    """Return the Artwork represented by node."""
    uid = node['id']
    name = node['name']
    x = node['transform']['ty']
    y = node['transform']['tx']

    if node['type'] == 'shape':
        if node['shape']['type'] == 'ellipse':
            width, height = 2 * node['shape']['cx'], 2 * node['shape']['cy']
            return Ellipse(uid, name, x, y, width, height)
        elif node['shape']['type'] == 'rect':
            width, height = node['shape']['width'], node['shape']['height']
            return Rectangle(uid, name, x, y, width, height)
        elif node['shape']['type'] == 'line':
            start_x, start_y = node['shape']['x1'], node['shape']['y1']
            end_x, end_y = node['shape']['x2'], node['shape']['y2']
            return Line(uid, start_x, start_y,
                        end_x, end_y, name, x, y)
        elif node['shape']['type'] == 'path':
            path_data = node['shape']['path']
            return Path(uid, path_data, name, x, y)
        elif node['shape']['type'] == 'compound':
            path = node['shape']['path']
            operation = node['shape']['operation']
            children = [extract_artwork(child)
                        for child in node['shape']['children']]
            return Compound(id, path, operation, children, name, x, y)
        else:
            raise UnknownShapeException("Error parsing unknown shape.")
    elif node['type'] == 'text':
        raw_text = node['text']['rawText']
        return Text(uid, raw_text, name, x, y)
    elif node['type'] == 'group':
        children = [extract_artwork(child)
                    for child in node['group']['children']]
        return Group(uid, name, x, y, children)
    else:
        raise UnknownShapeException("Error parsing unknown artwork.")


def extract_artboard(node, source):
    """Return the Artboard represented by node."""
    uid = node['id']
    name = node['name']
    width = None
    height = None
    x = None
    y = None
    if 'uxdesign#bounds' in node:
        width = node['uxdesign#bounds']['width']
        height = node['uxdesign#bounds']['height']
        x = node['uxdesign#bounds']['x']
        y = node['uxdesign#bounds']['y']

    viewport_height = None
    if 'uxdesign#viewport' in node:
        viewport_height = node['uxdesign#viewport']['height']

    artboard_file_path = "artwork/{}/graphics/graphicContent.agc".format(
        node['path'])
    artboard_file = source.read(artboard_file_path)
    artboard_data = json.loads(artboard_file)
    artworks = []
    for item in artboard_data['children']:
        for child in item['artboard']['children']:
            try:
                artwork = extract_artwork(child)
            except UnknownShapeException as shape_exception:
                print(shape_exception)
            except UnknownArtworkException as artwork_exception:
                print(artwork_exception)
            else:
                artworks.append(artwork)

    if name == 'pasteboard':
        return Artboard(uid, name, artworks=artworks)
    else:
        return Artboard(uid, name, width, height, Point(x, y), viewport_height, artworks)


def parse_file(path):
    source = zipfile.ZipFile(path, 'r')
    manifest_file = source.read("manifest")
    manifest_file_json = json.loads(manifest_file)
    resources_file = source.read("resources/graphics/graphicContent.agc")
    resources_file_json = json.loads(resources_file)

    # Extract project metadata
    project_name = manifest_file_json['name']
    thumbnail_image_path = manifest_file_json['components'][0]['path']
    preview_image_path = manifest_file_json['components'][1]['path']

    ## Extract color swatches
    color_swatches_node = resources_file_json['resources']['meta']['ux']['colorSwatches']
    color_swatches = []
    for node in color_swatches_node:
        value = node['value']
        color = Color(value['r'], value['g'], value['b'])
        color_swatches.append(color)

    # Extract artboard content
    artboards = []
    artboard_nodes = manifest_file_json['children'][0]['children']
    for artboard_node in artboard_nodes:
        artboard = extract_artboard(artboard_node, source)
        artboards.append(artboard)

    return XDFile(project_name, path, thumbnail_image_path, preview_image_path,
                  color_swatches, artboards)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="File to be extracted and parsed")
    args = parser.parse_args()

    assert os.path.isfile(args.source), "Source file cannot be found!"

    xd_file = parse_file(args.source)
