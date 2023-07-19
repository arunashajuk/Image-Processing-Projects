
"""
Perform image enhancement on ’moon.tif ’ using Laplacian in the frequency
domain.
"""

import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

def Laplacian_Mask(Image):
    height, width = Image.shape
    
    Laplacian = np.full((height, width),0)
    
    # Creating the Laplacian Mask
    
    for i in range(height):
        for j in range(width):
             d = math.sqrt((i-int(height)/2)**2 + (j-int(width)/2)**2) 
             Laplacian[i,j] = -1*(4*(math.pi**2)*(d**2))
             
    Laplacian_output = Image*Laplacian
    Laplacian_output_IFFT = np.fft.ifft2(Laplacian_output)
      
           
    # Decentering
    for i in range(height):
     for j in range(width):
        
        Laplacian_output_IFFT[i,j] = Laplacian_output_IFFT[i,j]*((-1)**(i+j))    
    
    # Normalizing values of Laplacian mask output 
    Laplacian_output_image  = cv2.normalize(np.float32(Laplacian_output_IFFT)  , None, -255, 255, norm_type=cv2.NORM_MINMAX)
     
    Laplacian_output_adjusted  = Laplacian_output_image [(int(height/2) - int(height/4)):(int(height/2) + int(height/4)), (int(width/2) - int(width/4)):(int(width/2) + int(width/4)) ]
     
    
    plt.imshow(np.log(abs(Laplacian_output_adjusted)), cmap='gray');    
    
    return Laplacian_output_image

Moon_Image = cv2.imread("moon.tif", 0)
height, width = Moon_Image.shape

# Zero Padding
Moon_pad = np.pad(np.array(Moon_Image), ((int(height/2),int(height/2)),(int(width/2),int(width/2))),'symmetric')

Moon_pad_centre = np.full((2*height, 2*width),0)

# Centering
for i in range(height*2):
    for j in range(width*2):
        
        Moon_pad_centre[i,j] = Moon_pad[i,j]*((-1)**(i+j))     

Moon_Image_FFT = np.fft.fft2(Moon_pad_centre)

Laplacian_output = Laplacian_Mask(Moon_Image_FFT)            
Laplacian_Enhancement =  Moon_pad - Laplacian_output

Laplacian_Enhancement_output = Laplacian_Enhancement[(int(height) - int(height/2)):(int(height) + int(height/2)), (int(width) - int(width/2)):(int(width) + int(width/2)) ]
Laplacian_Enhancement_output = np.clip(Laplacian_Enhancement_output, 0, 255)
Laplacian_Enhancement_output = Laplacian_Enhancement_output.astype('uint8')

plt.imshow(Laplacian_Enhancement_output, cmap='gray');
cv2.imwrite('Laplacian_Enhancement.tif',Laplacian_Enhancement_output)








