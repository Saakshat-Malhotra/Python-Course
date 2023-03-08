from PIL import Image, ImageFilter

img = Image.open("./astro.jpg")
print(img.size)
img.thumbnail((400, 400))
img.save("astro_thumbnail.jpg")
print(img.size)
