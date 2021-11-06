from PIL import Image
from settings import *

filepath = "GUI/pngs/battlebg.png"

# Image.open() can also open other image types
img = Image.open(filepath)
# WIDTH and HEIGHT are integers
resized_img = img.resize((HEIGHT, WIDTH))
resized_img.save(filepath)