# -*- coding: utf-8 -*-
"""
Perform following lowpass filtering(LPF) operations on ’alphabet.tif ’ with
cutoff frequencies set at radii values 10, 30, 60, 160, and 460:
(a) Ideal LPF
(b) Gaussian LPF
(c) Butterworth LPF(compare the effect of filter order)

"""

import numpy as np
import cv2
import math
import matplotlib.pyplot as plt


def Ideal_HPF(Image,cutoff):
    
    height, width = Image.shape  
    Ideal_HPF = np.full((height, width),0)
    
    # Creating the Ideal High Pass Filter Mask
    
    for i in range(height):
        for j in range(width):
             d = math.sqrt((i-int(height)/2)**2 + (j-int(width)/2)**2) 
             if (d >= cutoff):
                 Ideal_HPF[i,j] = 1
       
    Ideal_Highpass_output = Filter_Output(Image, Ideal_HPF)
    return Ideal_Highpass_output

    
def Gaussian_HPF(Image, cutoff):
    height, width = Image.shape
    
    Gaussian_HPF = Image.copy()
    
    # Creating the Gaussian Pass Filter Mask
    
    for i in range(height):
        for j in range(width):
             d_square = (i-int(height)/2)**2 + (j-int(width)/2)**2
             temp = -d_square/(2*(cutoff**2))             
             Gaussian_HPF[i,j] = 1 - math.exp(temp)
             
      
    Ideal_Highpass_output = Filter_Output(Image, Gaussian_HPF)
    
    plt.figure(num=None, figsize=(8, 6), dpi=80)
    plt.imshow(np.log(abs(Gaussian_HPF)), cmap='gray');
    
    return Ideal_Highpass_output
    
def Butterworth_HPF(Image, cutoff,order):
    height, width = Image.shape
    
    Butterworth_HPF = Image.copy()
    
    # Creating the Butterworth High Pass Filter Mask
    
    for i in range(height):
        for j in range(width):
             d = math.sqrt((i-int(height)/2)**2 + (j-int(width)/2)**2)
             
             # To combat zero division error
             if(d!=0):
                 temp = (cutoff/d)**(2*order)             
                 Butterworth_HPF[i,j] = 1/(1+temp)
              
             else:
                 Butterworth_HPF[i,j] = 0
    
    Ideal_Highpass_output = Filter_Output(Image, Butterworth_HPF)
    
    plt.figure(num=None, figsize=(8, 6), dpi=80)
    plt.imshow(np.log(abs(Butterworth_HPF)), cmap='gray');
    
    return Ideal_Highpass_output

def Filter_Output(Image, Mask):
    height, width = Image.shape
    
    High_Pass_output = Image*Mask
    Highpass_output_IFFT = np.fft.ifft2(High_Pass_output)
       
    
    # Decentering
    for i in range(height):
     for j in range(width):
        
        Highpass_output_IFFT[i,j] = Highpass_output_IFFT[i,j]*((-1)**(i+j))    
    
    Highpass_output_image = Highpass_output_IFFT[(int(height/2) - int(height/4)):(int(height/2) + int(height/4)), (int(width/2) - int(width/4)):(int(width/2) + int(width/4)) ]
    
    # Discarding imaginary values of image and limiting into gray scale range
    
    
    Highpass_output_image = np.clip(Highpass_output_image, 0, 255)
    Highpass_output_image = Highpass_output_image.astype('uint8')
    
    
    return Highpass_output_image
    
Alphabet_Image = cv2.imread("alphabet.tif", 0)
height, width = Alphabet_Image.shape

# Mirror Padding
Alphabet_pad = np.pad(np.array(Alphabet_Image), ((int(height/2),int(height/2)),(int(width/2),int(width/2))),'symmetric')

Alphabet_pad_centre = np.full((2*height, 2*width),0)

# Centering
for i in range(height*2):
    for j in range(width*2):
        
        Alphabet_pad_centre[i,j] = Alphabet_pad[i,j]*((-1)**(i+j))     

Alphabet_Image_FFT = np.fft.fft2(Alphabet_pad_centre)

Ideal_Highpass_60 = Ideal_HPF(Alphabet_Image_FFT, 60)       
cv2.imshow('Ideal_Highpass_60', abs(Ideal_Highpass_60))
cv2.imwrite('Ideal_Highpass_60.tif',Ideal_Highpass_60)
cv2.waitKey(0)

Ideal_Highpass_160 = Ideal_HPF(Alphabet_Image_FFT, 160)       
cv2.imshow('Ideal_Highpass_160', abs(Ideal_Highpass_160))
cv2.imwrite('Ideal_Highpass_160.tif',Ideal_Highpass_160)
cv2.waitKey(0)

Gaussian_Highpass_60 = Gaussian_HPF(Alphabet_Image_FFT, 60) 
cv2.imshow('Gaussian_Highpass_60', abs(Gaussian_Highpass_60))
cv2.imwrite('Gaussian_Highpass_60.tif',Gaussian_Highpass_60)
cv2.waitKey(0)

Gaussian_Highpass_160 = Gaussian_HPF(Alphabet_Image_FFT, 160) 
cv2.imshow('Gaussian_Highpass_160', abs(Gaussian_Highpass_160))
cv2.imwrite('Gaussian_Highpass_160.tif',Gaussian_Highpass_160)
cv2.waitKey(0)

Butterworth_Highpass_60_1 = Butterworth_HPF(Alphabet_Image_FFT, 60,1) 
cv2.imshow('Butterworth_Highpass_60_1', abs(Butterworth_Highpass_60_1))
cv2.imwrite('Butterworth_Highpass_60_1.tif',Butterworth_Highpass_60_1)
cv2.waitKey(0)

Butterworth_Highpass_160_1 = Butterworth_HPF(Alphabet_Image_FFT, 160,1) 
cv2.imshow('Butterworth_Highpass_160_1', abs(Butterworth_Highpass_160_1))
cv2.imwrite('Butterworth_Highpass_160_1.tif',Butterworth_Highpass_160_1)
cv2.waitKey(0)

Butterworth_Highpass_60_3 = Butterworth_HPF(Alphabet_Image_FFT, 60,3) 
cv2.imshow('Butterworth_Highpass_60_3', abs(Butterworth_Highpass_60_3))
cv2.imwrite('Butterworth_Highpass_60_3.tif',Butterworth_Highpass_60_3)
cv2.waitKey(0)

Butterworth_Highpass_160_3 = Butterworth_HPF(Alphabet_Image_FFT, 160,3) 
cv2.imshow('Butterworth_Highpass_160_3', abs(Butterworth_Highpass_160_3))
cv2.imwrite('Butterworth_Highpass_160_3.tif',Butterworth_Highpass_160_3)
cv2.waitKey(0)


Butterworth_Highpass_60_5 = Butterworth_HPF(Alphabet_Image_FFT, 60,5) 
cv2.imshow('Butterworth_Highpass_60_5', abs(Butterworth_Highpass_60_5))
cv2.imwrite('Butterworth_Highpass_60_5.tif',Butterworth_Highpass_60_5)
cv2.waitKey(0)

Butterworth_Highpass_160_5 = Butterworth_HPF(Alphabet_Image_FFT, 160,5) 
cv2.imshow('Butterworth_Highpass_160_5', abs(Butterworth_Highpass_160_5))
cv2.imwrite('Butterworth_Highpass_160_5.tif',Butterworth_Highpass_160_5)
cv2.waitKey(0)
