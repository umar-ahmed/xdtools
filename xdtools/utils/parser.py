"""
File parser.
"""

import json

from xdtools.artboard import Artboard

from xdtools.utils.point import Point

from xdtools.artwork.ellipse import Ellipse
from xdtools.artwork.rectangle import Rectangle
from xdtools.artwork.line import Line
from xdtools.artwork.text import Text
from xdtools.artwork.path import Path
from xdtools.artwork.group import Group
from xdtools.artwork.compound import Compound


class UnknownArtworkException(Exception):
    """Represents an exception where the type of shape is unknown."""
    pass


class UnknownShapeException(UnknownArtworkException):
    """Represents an exception where the type of shape is unknown."""
    pass


def parse_artwork(node):
    """Return the Artwork represented by node."""
    uid = node['id']
    name = node['name'] if 'name' in node else ''
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
            children = [parse_artwork(child)
                        for child in node['shape']['children']]
            return Compound(id, path, operation, children, name, x, y)
        else:
            raise UnknownShapeException("Error parsing unknown shape.")
    elif node['type'] == 'text':
        raw_text = node['text']['rawText']
        return Text(uid, raw_text, name, x, y)
    elif node['type'] == 'group':
        children = [parse_artwork(child)
                    for child in node['group']['children']]
        return Group(uid, name, x, y, children)
    else:
        raise UnknownShapeException("Error parsing unknown artwork.")


def parse_artboard(node, source):
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
                artwork = parse_artwork(child)
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
