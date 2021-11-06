from PIL import Image
from settings import *

filepath = "GUI/pngs/grass.png"

# Image.open() can also open other image types
img = Image.open(filepath)
# WIDTH and HEIGHT are integers
resized_img = img.resize((GRIDHEIGHT, GRIDHEIGHT))
resized_img.save(filepath)