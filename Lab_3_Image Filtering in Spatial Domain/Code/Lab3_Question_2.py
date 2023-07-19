"""
Add different types of noises to the input image using inbuilt functions in
python.

"""

import cv2
import numpy as np
from skimage.util import random_noise
 
  
# Load the image
Image_Cameraman = cv2.imread("Cameraman.png")
 
#Using skimage module

# 1)Add salt-and-pepper noise to the image.
Image_Cameraman_saltpepper = random_noise(Image_Cameraman, mode='s&p',amount=0.01)
 
Image_Cameraman_saltpepper = np.array(255*Image_Cameraman_saltpepper, dtype = 'uint8') 
cv2.imshow('Image_Cameraman_saltpepper',Image_Cameraman_saltpepper)
cv2.imwrite('Cameraman_Noise_Salt_and_Pepper.jpeg',Image_Cameraman_saltpepper)
cv2.waitKey(0)


# 2) Add speckle noise to the image.
Image_Cameraman_speckle = random_noise(Image_Cameraman, mode='speckle',mean= 0.5)
 
Image_Cameraman_speckle = np.array(255*Image_Cameraman_speckle, dtype = 'uint8')
cv2.imshow('Image_Cameraman_speckle',Image_Cameraman_speckle)
cv2.imwrite('Cameraman_Noise_Speckle.jpeg',Image_Cameraman_speckle)
cv2.waitKey(0)


#3) Add gaussian noise to the image.
Image_Cameraman_gaussian = random_noise(Image_Cameraman, mode='gaussian')
 
Image_Cameraman_gaussian = np.array(255*Image_Cameraman_gaussian, dtype = 'uint8')
cv2.imshow('Image_Cameraman_gaussian',Image_Cameraman_gaussian)
cv2.imwrite('Cameraman_Noise_Gaussian.jpeg',Image_Cameraman_gaussian)
cv2.waitKey(0)

# 4) Add poisson noise to the image.
Image_Cameraman_poisson = random_noise(Image_Cameraman, mode='poisson')
 
Image_Cameraman_poisson = np.array(255*Image_Cameraman_poisson, dtype = 'uint8')
cv2.imshow('Image_Cameraman_poisson',Image_Cameraman_poisson)
cv2.imwrite('Cameraman_Noise_Poisson.jpeg',Image_Cameraman_poisson)
cv2.waitKey(0)