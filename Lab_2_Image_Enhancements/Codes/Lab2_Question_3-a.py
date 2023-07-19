'''Develop programs for the following image enhancement operations.
(a) Brightness enhancement
(Use pollengrains.tif image)
Increase the intensity value at each location of the image, to obtain the brightness
enhanced image'''

from PIL import Image

Pollen_Image = Image.open("pollen_grains.tif")
Pollen_Image_Enhanced = Pollen_Image.copy()
Enhancement_factor = int(input('Input the Enhancement intensity factor\n'))

Pollen_Image_Enhanced.show()

height, width  = Pollen_Image.size

for i in range(width):
    for j in range(height):
        temp = Pollen_Image.getpixel((j,i)) + Enhancement_factor
        
        Pollen_Image_Enhanced.putpixel((j,i),(temp))
    
Pollen_Image_Enhanced.show()

Pollen_Image_Enhanced.save("Pollen_Image_Enhanced.tif")