from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img1 = img.convert('L')
print(filtered_img1.size)
resize = filtered_img1.resize((100, 100))
filtered_img1.save("grey.png", "png")
resize.save("grey1.png", "png")
filtered_img.save("blur.png", "png")
# filtered_img.show()
