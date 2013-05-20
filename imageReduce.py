import os
from PIL import Image

def reduceQuality(file, qual):
	img = Image.open(file)
	img.thumbnail((img.Width,img.Height), Image.ANTIALIAS).save(file, "JPEG", quality=qual)
