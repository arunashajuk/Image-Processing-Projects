"""
Created on Mon Oct 18 02:01:24 2021

@author: arunashajukPerform the following image enhancement operations on ’chest.tif ’.
(a) Unsharp masking
(b) Highboost filtering
(c) High-frequency emphasis filtering
"""

import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

def Gaussian_LPF(Image, cutoff):
    height, width = Image.shape
    
    Gaussian_LPF = Image.copy()
    
    # Creating the Ideal Low Pass Filter Mask
    
    for i in range(height):
        for j in range(width):
             d_square = (i-int(height)/2)**2 + (j-int(width)/2)**2
             temp = -d_square/(2*(cutoff**2))             
             Gaussian_LPF[i,j] = math.exp(temp)
             
      
    Ideal_Lowpass_output = Filter_Output(Image, Gaussian_LPF)
    
    plt.figure(num=None, figsize=(8, 6), dpi=80)
    plt.imshow(np.log(abs(Gaussian_LPF)), cmap='gray');
    
    return Ideal_Lowpass_output

def High_Freq_Emphasis(Image, cutoff):
    height, width = Image.shape
    
    Gaussian_HPF = Image.copy()
    
    # Creating the Ideal Low Pass Filter Mask
    
    for i in range(height):
        for j in range(width):
             d_square = (i-int(height)/2)**2 + (j-int(width)/2)**2
             temp = -d_square/(2*(cutoff**2))             
             Gaussian_HPF[i,j] = 1 - math.exp(temp)
             
    High_Pass_output = Image*Gaussian_HPF
    
    High_Freq_Emp_output = Image + 2*High_Pass_output
    High_Freq_Emp_output = np.fft.ifft2(High_Freq_Emp_output)
       
    
    # Decentering
    for i in range(height):
     for j in range(width):
        
        High_Freq_Emp_output[i,j] = High_Freq_Emp_output[i,j]*((-1)**(i+j))    
    
    High_Freq_Emp_output = High_Freq_Emp_output[(int(height/2) - int(height/4)):(int(height/2) + int(height/4)), (int(width/2) - int(width/4)):(int(width/2) + int(width/4)) ]
    
    # Discarding imaginary values of image and limiting into gray scale range
        
    High_Freq_Emp_output= np.clip(High_Freq_Emp_output, 0, 255)
    High_Freq_Emp_output = High_Freq_Emp_output.astype('uint8')
    
    
   
    return High_Freq_Emp_output

def Filter_Output(Image, Mask):
    height, width = Image.shape
    
    Low_Pass_output = Image*Mask
    Lowpass_output_IFFT = np.fft.ifft2(Low_Pass_output)
       
    
    # Decentering
    for i in range(height):
     for j in range(width):
        
        Lowpass_output_IFFT[i,j] = Lowpass_output_IFFT[i,j]*((-1)**(i+j))    
    
    Lowpass_output_image = Lowpass_output_IFFT[(int(height/2) - int(height/4)):(int(height/2) + int(height/4)), (int(width/2) - int(width/4)):(int(width/2) + int(width/4)) ]
    
    # Discarding imaginary values of image and limiting into gray scale range
    
    
    Lowpass_output_image = np.clip(Lowpass_output_image, 0, 255)
    Lowpass_output_image = Lowpass_output_image.astype('uint8')
    
    
    return Lowpass_output_image

Chest_Image = cv2.imread("chest.tif", 0)
height, width = Chest_Image.shape

# Mirror Padding
Chest_pad = np.pad(np.array(Chest_Image), ((int(height/2),int(height/2)),(int(width/2),int(width/2))),'symmetric')

Chest_pad_centre = np.full((2*height, 2*width),0)

# Centering
for i in range(height*2):
    for j in range(width*2):
        
        Chest_pad_centre[i,j] = Chest_pad[i,j]*((-1)**(i+j))     

Chest_Image_FFT = np.fft.fft2(Chest_pad_centre)

Chest_pad_centre = Chest_pad_centre[(int(height) - int(height/2)):(int(height) + int(height/2)), (int(width) - int(width/2)):(int(width) + int(width/2)) ]
Lowpass_Output = Gaussian_LPF(Chest_Image_FFT , 60)
G_mask = Chest_pad_centre - Lowpass_Output


unsharp_output = Chest_pad_centre + G_mask
unsharp_output = np.clip(unsharp_output, 0, 255)
unsharp_output = unsharp_output.astype('uint8')

highboost_output = Chest_pad_centre + 2*G_mask
highboost_output = np.clip(highboost_output, 0, 255)
highboost_output = highboost_output.astype('uint8')

high_freq_emphasis = High_Freq_Emphasis(Chest_Image_FFT , 60)

plt.subplot(3, 1, 1)
plt.imshow(unsharp_output, cmap="gray")
cv2.imwrite('unsharp_output.tif',unsharp_output)


plt.subplot(3, 1, 2)
plt.imshow(highboost_output , cmap="gray")
cv2.imwrite('highboost_output .tif',highboost_output )

plt.subplot(3,1,3)
plt.imshow(high_freq_emphasis , cmap="gray")
cv2.imwrite('high_freq_emphasis.tif',high_freq_emphasis)
