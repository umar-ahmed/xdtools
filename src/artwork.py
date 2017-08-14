"""Contains abstract Artwork class used to represent artwork in a .xd project"""

class Artwork:
	"""
	A visible element in a .xd project
	
	=== Attributes ===
	name - The name of this artwork; this is the name that XD for its layers.
	id - The id of this artwork.
	position - The position of this artwork on the artboard or pasteboard.
	width - The width of this artwork, in pixels.
	height - The height of this artwork, in pixels.
	styles - The styles of this artwork.

	=== Operations ===
	move(x, y) - Move the Artwork to a specific coordinate on the artboard or
		pasteboard.
	
	"""
	def __init__(self):
		