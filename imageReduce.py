import os
from PIL import Image

def reduceQuality(file, qual):
	img = Image.open(file)
	img.resize(img.size, Image.ANTIALIAS).save(file, "JPEG", quality=qual)
