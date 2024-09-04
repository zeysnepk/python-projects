# Photo Filtering and Photo Cropping with Pillow Module

from PIL import Image, ImageFilter


image = Image.open("cars.jpg")
 
#image.show() #shows image on pc

image.save("carsCopy.jpg")

image.rotate(180).save("carsRotate.jpg") #rotates the image 180 degrees

image.convert(mode = "L").save("carsBlackWhite.jpg") #converts the image to black and white

sizeOfImage = (400,400)
image.thumbnail(sizeOfImage)
image.save("carsSize.jpg")

image.filter(ImageFilter.GaussianBlur(10)).save("carsBlur.jpg") #blurring the image

image = Image.open("cars.jpg")

cropSize = (30, 300, 500, 1000)
image.crop(cropSize).save("carsCrop.jpg") #crop the image






 