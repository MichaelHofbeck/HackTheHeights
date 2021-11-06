from PIL import Image
from settings import *

filepath = "GUI/pngs/teacher1.png"

# Image.open() can also open other image types
img = Image.open(filepath)
# WIDTH and HEIGHT are integers
resized_img = img.resize((GRIDHEIGHT * 2, GRIDHEIGHT * 2))
resized_img.save(filepath)