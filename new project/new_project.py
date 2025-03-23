from PIL import Image


image = Image.open('Holden_John_D_Salvador.webp')
image.show()
image.save('Holden.png')
image = Image.open('Holden.png')
image.show()
