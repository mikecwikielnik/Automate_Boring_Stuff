"""
MANIPULATING IMAGES

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 447). No Starch Press. Kindle Edition. 
"""

from PIL import ImageColor

ImageColor.getcolor('red', 'RGBA')
ImageColor.getcolor('RED', 'RGBA')
ImageColor.getcolor('Black', 'RGBA')
ImageColor.getcolor('chocolate', 'RGBA')
ImageColor.getcolor('CornflowerBlue', 'RGBA')

# Manipulating Images with Pillow

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 450). No Starch Press. Kindle Edition. 

from PIL import Image

catIm = Image.open('zophie.png')

# Working with the Image Data Type

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 451). No Starch Press. Kindle Edition. 

from PIL import Image

catIm = Image.open('zophie.png')
catIm.size
width, height = catIm.size
width
height
catIm.filename  
catIm.format
catIm.format_description
catIm.save('zophie.jpg')

from PIL import Image

im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')