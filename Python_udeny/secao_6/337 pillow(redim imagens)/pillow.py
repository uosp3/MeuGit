# https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/36459274#questions/19506542
# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / ' new.jpg'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info['exif']  # informações da imagem

# width     new_width
# height    ??
new_width = 640
new_height = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # exif=exif,
)
