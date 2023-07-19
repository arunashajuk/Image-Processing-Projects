''' Question 1) Display the negative of an image
(Use mammogram.tif image)
(Hint:To obtain the negative of an image, each pixel value is subtracted from the maximum pixel value (for eg. 255 for a grayscale image) and the difference is used as the
pixel value in the output image. In the output image, dark areas become lighter and light
areas become darker.) '''

from PIL import Image

Mammogram_Image = Image.open("mammogram.tif")

# Pixel with maximum intensity in image

Max_pixel = max(Image.Image.getextrema(Mammogram_Image))

Negative_Image = Mammogram_Image.copy()
height, width = Mammogram_Image.size

# Subtracting pixel values from maximum pixel intensity to invert image

for i in range(width):
    for j in range(height):
        temp = Max_pixel- Mammogram_Image.getpixel((j,i))
        
        Negative_Image.putpixel((j,i),(temp))

Negative_Image.save("Mammogram_Inverted_Image.tif")
 
Mammogram_Image.show()
Negative_Image.show()


