"""
File parser.
"""

import zipfile
import json
import argparse
import os
from ellipse import Ellipse
from rectangle import Rectangle
from line import Line
from text import Text
from path import Path
from group import Group


def extract_artwork(node):
    if node['type'] == 'shape':
        if node['shape']['type'] == 'ellipse':
            uid = node['id']
            name = node['name']
            x, y = node['transform']['tx'], node['transform']['ty']
            width, height = 2 * node['shape']['cx'], 2 * node['shape']['cy']
            return Ellipse(uid, name, x, y, width, height)
        elif node['shape']['type'] == 'rect':
            uid = node['id']
            name = node['name']
            x, y = node['transform']['tx'], node['transform']['ty']
            width, height = node['shape']['width'], node['shape']['height']
            return Rectangle(uid, name, x, y, width, height)
        elif node['shape']['type'] == 'line':
            uid = node['id']
            name = node['name']
            x, y = node['transform']['tx'], node['transform']['ty']
            start_x, start_y = node['shape']['x1'], node['shape']['y1']
            end_x, end_y = node['shape']['x2'], node['shape']['y2']
            return Line(uid, start_x, start_y,
                        end_x, end_y, name, x, y)
        elif node['shape']['type'] == 'path':
            uid = node['id']
            name = node['name']
            x, y = node['transform']['tx'], node['transform']['ty']
            path_data = node['shape']['path']
            return Path(uid, path_data, name, x, y)
        else:
            print(node)
    elif node['type'] == 'text':
        uid = node['id']
        name = node['name']
        x, y = node['transform']['tx'], node['transform']['ty']
        raw_text = node['text']['rawText']
        return Text(uid, raw_text, name, x, y)
    elif node['type'] == 'group':
        uid = node['id']
        name = node['name']
        x, y = node['transform']['tx'], node['transform']['ty']
        children = []
        for child in node['group']['children']:
            children.append(extract_artwork(child))
        return Group(uid, name, x, y, children)
    else:
        print(node)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="File to be extracted and parsed")
    args = parser.parse_args()

    assert os.path.isfile(args.source), "Source file cannot be found!"

    source = zipfile.ZipFile(args.source, 'r')
    manifest_file = source.read("manifest")
    artboards = json.loads(manifest_file)['children'][0]['children']

    for artboard in artboards:
        artboard_file_path = "artwork/{}/graphics/graphicContent.agc".format(
            artboard['path'])
        artboard_file = source.read(artboard_file_path)
        artboard_data = json.loads(artboard_file)
        print(">>>", artboard['name'])

        layers = []

        for item in artboard_data['children']:
            for child in item['artboard']['children']:
                artwork = extract_artwork(child)
                layers.append(artwork)

        for layer in layers:
            print(layer)
