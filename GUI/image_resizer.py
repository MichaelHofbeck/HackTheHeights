from PIL import Image
from GUI.settings import *

def image_resizer(filepath, width_size = TILESIZE, height_size = TILESIZE):
    img = Image.open(filepath)
    resized_img = img.resize((width_size, height_size))
    resized_img.save(filepath[0:-4] + "-resized.png")