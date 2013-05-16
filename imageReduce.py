import os
from PIL import Image

def reduceQuality(file, qual):
	img = Image.open(file).thumbnail((newWidth,newHeight), Image.ANTIALIAS).save(file, "JPEG", quality=qual)