"""
File parser.
"""

import json

from xdtools.artboard import Artboard
from xdtools.artwork import Ellipse, Rectangle, Line, Text, Path, Group, Compound
from xdtools.style import ColorFill, GradientFill, ColorStroke, DropShadow, Blur

from xdtools.utils import Point, Color, Gradient, GradientStop
from xdtools.utils.exceptions import *


def get_resources_file_json(source):
    """Return the resources JSON file of the provided source file"""
    if source is not None:
        resources_file = source.read(
            "resources/graphics/graphicContent.agc")
        return json.loads(resources_file)
    else:
        raise Exception()


def get_manifest_file_json(source):
    """Return the manifest JSON file of the provided source file"""
    if source is not None:
        manifest_file = source.read("manifest")
        return json.loads(manifest_file)
    else:
        raise Exception()


def parse_color_swatches(source):
    """Return a list of Color swatches in the provided source file."""
    resources_file_json = get_resources_file_json(source)
    color_swatches_node = resources_file_json['resources']['meta']['ux']['colorSwatches']
    color_swatches = []
    for node in color_swatches_node:
        value = node['value']
        color = Color(value['r'], value['g'], value['b'])
        color_swatches.append(color)
    return color_swatches


def parse_gradients(source):
    """Return a list of Gradients in the provided source file."""
    resources_file_path = "resources/graphics/graphicContent.agc"
    resources_file = source.read(resources_file_path)
    resources_json = json.loads(resources_file)
    gradients_json = resources_json['resources']['gradients']

    gradients = []

    for uid, gradient_node in gradients_json.items():
        type_ = gradient_node['type']

        gradient_stops = []
        for stop_json in gradient_node['stops']:
            offset = stop_json['offset']
            color_json = stop_json['color']['value']
            gradient_stop = GradientStop(
                offset, color_json['r'], color_json['g'], color_json['b'])
            gradient_stops.append(gradient_stop)

        gradient = Gradient(uid, type_, gradient_stops)
        gradients.append(gradient)

    return gradients


def parse_styles(node, source):
    """Return the Styles represented by node."""
    styles = []
    for key, value in node.items():
        if key == 'fill':
            fill_type = value['type']
            if fill_type == 'solid':
                color_node = value['color']['value']
                color_fill = ColorFill(
                    color_node['r'], color_node['g'], color_node['b'])
                styles.append(color_fill)
            elif fill_type == 'gradient':
                x1 = value['gradient']['x1']
                y1 = value['gradient']['y1']
                start = Point(x1, y1)
                x2 = value['gradient']['x2']
                y2 = value['gradient']['y2']
                end = Point(x2, y2)
                gradient_uid = value['gradient']['ref']
                gradients = parse_gradients(source)
                gradient_fill = None
                for gradient in gradients:
                    if gradient.uid == gradient_uid:
                        gradient_fill = GradientFill(start, end, gradient)
                if gradient_fill is not None:
                    styles.append(gradient_fill)
            else:
                raise UnknownFillTypeException('Unable to parse fill: ' + key)
        elif key == 'stroke':
            width = value['width']
            align = 'inside'
            if 'align' in value:
                align = value['align']
            color_node = value['color']['value']
            color_stroke = ColorStroke(width, align, color_node['r'],
                                       color_node['g'], color_node['b'])
            styles.append(color_stroke)
        elif key == 'filters':
            for filter_ in value:
                if filter_['type'] == 'dropShadow':
                    for drop_shadow_json in filter_['params']['dropShadows']:
                        offset_x = drop_shadow_json['dx']
                        offset_y = drop_shadow_json['dy']
                        blur_radius = drop_shadow_json['r']
                        color_node = drop_shadow_json['color']['value']
                        color = Color(
                            color_node['r'], color_node['g'], color_node['b'])
                        drop_shadow = DropShadow(offset_x, offset_y, blur_radius, color)
                        styles.append(drop_shadow)
                elif filter_['type'] == 'uxdesign#blur':
                    blur_json = filter_['params']
                    amount = blur_json['blurAmount']
                    brightness = blur_json['brightnessAmount']
                    fill_opacity = blur_json['fillOpacity']
                    background_effect = blur_json['backgroundEffect']
                    blur = Blur(amount, brightness, fill_opacity, background_effect)
                    styles.append(blur)
                else:
                    raise UnknownFilterTypeException(
                        'Unable to parse filter: ' + key)
        # elif key == 'font':
        #     raise NotImplementedError('font not supported yet')
        else:
            raise UnknownStyleException('Unable to parse the style: ' + key)

    return styles


def parse_artwork(node, source):
    """Return the Artwork represented by node."""
    uid = node['id']
    name = node['name'] if 'name' in node else ''
    x = node['transform']['ty']
    y = node['transform']['tx']

    artwork = None

    if node['type'] == 'shape':
        if node['shape']['type'] == 'ellipse':
            width, height = 2 * node['shape']['cx'], 2 * node['shape']['cy']
            artwork = Ellipse(uid, name, x, y, width, height)
        elif node['shape']['type'] == 'rect':
            width, height = node['shape']['width'], node['shape']['height']
            artwork = Rectangle(uid, name, x, y, width, height)
        elif node['shape']['type'] == 'line':
            start_x, start_y = node['shape']['x1'], node['shape']['y1']
            end_x, end_y = node['shape']['x2'], node['shape']['y2']
            artwork = Line(uid, start_x, start_y,
                           end_x, end_y, name, x, y)
        elif node['shape']['type'] == 'path':
            path_data = node['shape']['path']
            artwork = Path(uid, path_data, name, x, y)
        elif node['shape']['type'] == 'compound':
            path = node['shape']['path']
            operation = node['shape']['operation']
            children = [parse_artwork(child, source)
                        for child in node['shape']['children']]
            return Compound(uid, path, operation, children, name, x, y)
        else:
            raise UnknownShapeException("Error parsing unknown shape.")
    elif node['type'] == 'text':
        raw_text = node['text']['rawText']
        artwork = Text(uid, raw_text, name, x, y)
    elif node['type'] == 'group':
        children = [parse_artwork(child, source)
                    for child in node['group']['children']]
        artwork = Group(uid, name, x, y, children)
    else:
        raise UnknownShapeException("Error parsing unknown artwork.")

    try:
        if 'style' in node.keys():
            styles = parse_styles(node['style'], source)
            artwork.add_styles(styles)
    except XDToolsException as e:
        print('Error processing styles.', e)

    return artwork


def parse_artboards(source):
    """Return a list of Artboards that are in the provided source file."""
    artboards = []
    manifest_file_json = get_manifest_file_json(source)
    artboard_nodes = manifest_file_json['children'][0]['children']
    for artboard_node in artboard_nodes:
        artboard = parse_artboard(artboard_node, source)
        artboards.append(artboard)
    return artboards


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
                artwork = parse_artwork(child, source)
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


def parse_name(source):
    """Return the name of the XD project for the provided source file."""
    manifest_file_json = get_manifest_file_json(source)
    return manifest_file_json['name']


def parse_thumbnail_path(source):
    """Return the thumbnail path of the XD project for the provided source file."""
    manifest_file_json = get_manifest_file_json(source)
    return manifest_file_json['components'][0]['path']


def parse_preview_path(source):
    """Return the preview path of the XD project for the provided source file."""
    manifest_file_json = get_manifest_file_json(source)
    return manifest_file_json['components'][1]['path']
