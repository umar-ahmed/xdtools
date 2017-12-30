"""
Contains the definition of class Artwork.
"""


class DuplicateStyleTypeException(Exception):
    """
    Represents an Exception resulting from duplicate style types in the same
    artwork.
    """
    pass


class Artwork:
    """Represents an Artwork on an Artboard."""

    def __init__(self, uid, name):
        """Instantiates this Artwork."""
        self.uid = uid
        self.name = name
        self.styles = {}

    def add_style(self, style):
        """
        Add style to this Artwork's styles.

        Raises DuplicateStyleTypeException.
        """
        if style.type not in self.styles:
            self.styles[style.type] = style
        else:
            raise DuplicateStyleTypeException(
                str.format('There already exists a style of type ' + style.type))

    def add_styles(self, styles):
        """Add all Styles in styles to this Artwork."""
        try:
            for style in styles:
                self.add_style(style)
        except DuplicateStyleTypeException:
            print('Error adding styles.')
            exit()

