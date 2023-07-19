
'''Brightness slicing
(Use kidney.tif image)
Perform brightness enhancement, not for all the pixels, but only for pixels having
an intensity value within a certain range. (say for only pixels of intensity between
100 and 150).'''

from PIL import Image

Kidney_Image = Image.open("kidney.tif")
Kidney_without_Back = Kidney_Image.copy()
Kidney_with_Back = Kidney_Image.copy()

# With and Without Background
l= int(input('Enter the range of pixel intensities for Brightness Slicing\n'))
h = int(input(''))
Enhancement_factor = int(input('Input the Enhancement intensity\n'))
height, width = Kidney_Image.size

for i in range(width):
    for j in range(height):
        
        temp = Kidney_Image.getpixel((j,i))
        if temp in range(l,h+1):
            Kidney_without_Back.putpixel((j,i),(temp + Enhancement_factor))
            Kidney_with_Back.putpixel((j,i),(temp + Enhancement_factor))
        else:
             Kidney_with_Back.putpixel((j,i),(0))
        
        
Kidney_without_Back.show()
Kidney_with_Back.show()

Kidney_without_Back.save("Kidney_without_Back.tif")
Kidney_with_Back.save("Kidney_with_Back.tif")
