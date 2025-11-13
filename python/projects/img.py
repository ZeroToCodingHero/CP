from PIL import Image

# Location of the image
img = Image.open('test_img.jpg')

# size of the image
print(img.size)
# format of the image
print(img.format)

img.save('test_img.jpeg')

# opens the image
img.show()



# pip install pillow