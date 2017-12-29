# XD Tools

**This is currently a WIP.** XD Tools is an unofficial Python API for Adobe XD. It provides the ability to parse and read data from `.xd` files that are created by Adobe XD using Python 3. As Adobe XD is constantly changing each month with new features, this API will inevitably change in order to stay up-to-date, so please report issues on GitHub if you find any.

## Installation

```
pip install xdtools
```

## Example Usage

### Printing the name of project

```python
from xdtools import XDFile
with XDFile('path/to/file.xd', 'r') as xd:
    print(xd.name)
```

### Printing the names of artboards

```python
from xdtools import XDFile
with XDFile('path/to/file.xd', 'r') as xd:
    for artboard in xd.artboards:
      print(artboard.name)
```

### Printing the color swatches

```python
from xdtools import XDFile
with XDFile('path/to/file.xd', 'r') as xd:
    for color_swatch in xd.color_swatches:
      print(color_swatch)
```

## Planned Features

### Read data from an XD file

* Project Name
* Fonts
* Colors
* Gradients
* Symbols
* Images
* Preview
* Artboards
  * Amount
  * Names
  * Dimensions
  * Position
  * Viewport Size
  * Artwork
    * Name
    * Type
    * Specific Attributes (eg. letter spacing, etc.)
    * Dimensions
    * Position
    * Stroke
    * Fill
    * Opacity
    * Filters
* Interactions
  * From
  * To
  * Transition
  * Duration
  * Easing
