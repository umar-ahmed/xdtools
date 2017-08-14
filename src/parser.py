"""
File parser.
"""

import zipfile
import json
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("source", help="File to be extracted and parsed")
args = parser.parse_args()

assert os.path.isfile(args.source), "Source file cannot be found!"

source = zipfile.ZipFile(args.source, 'r')
manifest_file = source.read("manifest")
artboards = json.loads(manifest_file)['children'][0]['children']

for artboard in artboards:
    artboard_file_path = "artwork/{}/graphics/graphicContent.agc".format(artboard['path'])
    artboard_file = source.read(artboard_file_path)
    artboard_data = json.loads(artboard_file)
    print(">>>", artboard['name'])
    for item in artboard_data['children']:
        for c in item['artboard']['children']:
            if c['type'] == 'text':
                font = c['style']['font']
                print('-', font['family'], font['style'], font['size'])
