''' 2. Plot the histogram of an image.
(Use cameraman.tif image.)
(Histogram of an image is a graph showing the number of pixels in an image at each
different intensity value found in that image. For example consider a 3 × 3 image: '''

from PIL import Image, ImageOps

import matplotlib.pyplot as plt

Cameraman_Image = Image.open("cameraman.png")
Cameraman_gray =  ImageOps.grayscale(Cameraman_Image)
Cameraman_gray.show()
height, width = Cameraman_gray.size

# empty list to hold the frequency of each pixel intensity
Hist_density = []

# for each pixel intensity in range (0-255) , loop is run throughout th image to calculate the count of that intensity
for pix_intensity in range(0,256):
    density = 0
    for i in range(width):
         for j in range(height):
           if (Cameraman_gray.getpixel((j,i))== pix_intensity):
               density = density + 1
               
    # total count of each pixel intensity appended
    Hist_density.append(density)
    
#print(Hist_density)
range_p = range(0,256)

plt.plot(range_p, Hist_density)

