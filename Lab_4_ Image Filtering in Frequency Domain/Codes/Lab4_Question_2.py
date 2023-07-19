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


def Ideal_LPF(Image,cutoff):
    height, width = Image.shape
    
    Ideal_LPF = np.full((height, width),0)
    
    # Creating the Ideal Low Pass Filter Mask
    
    for i in range(height):
        for j in range(width):
             d = math.sqrt((i-int(height)/2)**2 + (j-int(width)/2)**2) 
             if (d <= cutoff):
                 Ideal_LPF[i,j] = 1
       
    Ideal_Lowpass_output = Filter_Output(Image, Ideal_LPF)
    return Ideal_Lowpass_output

    
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
    
def Butterworth_LPF(Image, cutoff,order):
    height, width = Image.shape
    
    Butterworth_LPF = Image.copy()
    
    # Creating the Butterworth Low Pass Filter Mask
    
    for i in range(height):
        for j in range(width):
             d = math.sqrt((i-int(height)/2)**2 + (j-int(width)/2)**2)
             temp = (d/cutoff)**(2*order)       
             Butterworth_LPF[i,j] = 1/(1+temp)             
      
    Ideal_Lowpass_output = Filter_Output(Image, Butterworth_LPF)
    
    plt.figure(num=None, figsize=(8, 6), dpi=80)
    plt.imshow(np.log(abs(Butterworth_LPF)), cmap='gray');
    
    return Ideal_Lowpass_output
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

Ideal_Lowpass_10 = Ideal_LPF(Alphabet_Image_FFT, 10)       
cv2.imshow('Ideal_Lowpass_10', abs(Ideal_Lowpass_10))
cv2.imwrite('Ideal_Lowpass_10.tif',Ideal_Lowpass_10)
cv2.waitKey(0)
 
Ideal_Lowpass_30 = Ideal_LPF(Alphabet_Image_FFT, 30)       
cv2.imshow('Ideal_Lowpass_30', abs(Ideal_Lowpass_30))
cv2.imwrite('Ideal_Lowpass_30.tif',Ideal_Lowpass_30)
cv2.waitKey(0)

Ideal_Lowpass_60 = Ideal_LPF(Alphabet_Image_FFT, 60)       
cv2.imshow('Ideal_Lowpass_60', abs(Ideal_Lowpass_60))
cv2.imwrite('Ideal_Lowpass_60.tif',Ideal_Lowpass_60)
cv2.waitKey(0)

Ideal_Lowpass_160 = Ideal_LPF(Alphabet_Image_FFT, 160)       
cv2.imshow('Ideal_Lowpass_160', abs(Ideal_Lowpass_160))
cv2.imwrite('Ideal_Lowpass_160.tif',Ideal_Lowpass_160)
cv2.waitKey(0)

Ideal_Lowpass_460 = Ideal_LPF(Alphabet_Image_FFT, 460)       
cv2.imshow('Ideal_Lowpass_460', abs(Ideal_Lowpass_460))
cv2.imwrite('Ideal_Lowpass_460.tif',Ideal_Lowpass_460)
cv2.waitKey(0)

Gaussian_Lowpass_10 = Gaussian_LPF(Alphabet_Image_FFT, 10)       
cv2.imshow('Gaussian_Lowpass_10', abs(Gaussian_Lowpass_10))
cv2.imwrite('Gaussian_Lowpass_10.tif',Gaussian_Lowpass_10)
cv2.waitKey(0)

Gaussian_Lowpass_30 = Gaussian_LPF(Alphabet_Image_FFT, 30)       
cv2.imshow('Gaussian_Lowpass_30', abs(Gaussian_Lowpass_30))
cv2.imwrite('Gaussian_Lowpass_30.tif',Gaussian_Lowpass_30)
cv2.waitKey(0)

Gaussian_Lowpass_60 = Gaussian_LPF(Alphabet_Image_FFT, 60)       
cv2.imshow('Gaussian_Lowpass_60', abs(Gaussian_Lowpass_60))
cv2.imwrite('Gaussian_Lowpass_60.tif',Gaussian_Lowpass_60)
cv2.waitKey(0)

Gaussian_Lowpass_160 = Gaussian_LPF(Alphabet_Image_FFT, 160)       
cv2.imshow('Gaussian_Lowpass_160', abs(Gaussian_Lowpass_160))
cv2.imwrite('Gaussian_Lowpass_160.tif',Gaussian_Lowpass_160)
cv2.waitKey(0)

Gaussian_Lowpass_460 = Gaussian_LPF(Alphabet_Image_FFT, 460)       
cv2.imshow('Gaussian_Lowpass_460', abs(Gaussian_Lowpass_460))
cv2.imwrite('Gaussian_Lowpass_460.tif',Gaussian_Lowpass_460)
cv2.waitKey(0)

Butterworth_Lowpass_10_1 = Butterworth_LPF(Alphabet_Image_FFT, 10,1)       
cv2.imshow('Butterworth_Lowpass_10_1', abs(Butterworth_Lowpass_10_1))
cv2.imwrite('Butterworth_Lowpass_10_1.tif',Butterworth_Lowpass_10_1)
cv2.waitKey(0)

Butterworth_Lowpass_30_1 = Butterworth_LPF(Alphabet_Image_FFT, 30,1)       
cv2.imshow('Butterworth_Lowpass_30_1', abs(Butterworth_Lowpass_30_1))
cv2.imwrite('Butterworth_Lowpass_30_1.tif',Butterworth_Lowpass_30_1)
cv2.waitKey(0)

Butterworth_Lowpass_60_1 = Butterworth_LPF(Alphabet_Image_FFT, 60,1)       
cv2.imshow('Butterworth_Lowpass_60_1', abs(Butterworth_Lowpass_60_1))
cv2.imwrite('Butterworth_Lowpass_60_1.tif',Butterworth_Lowpass_60_1)
cv2.waitKey(0)

Butterworth_Lowpass_160_1 = Butterworth_LPF(Alphabet_Image_FFT, 160,1)       
cv2.imshow('Butterworth_Lowpass_160_1', abs(Butterworth_Lowpass_160_1))
cv2.imwrite('Butterworth_Lowpass_160_1.tif',Butterworth_Lowpass_160_1)
cv2.waitKey(0)

Butterworth_Lowpass_460_1 = Butterworth_LPF(Alphabet_Image_FFT, 460,1)       
cv2.imshow('Butterworth_Lowpass_460_1', abs(Butterworth_Lowpass_460_1))
cv2.imwrite('Butterworth_Lowpass_460_1.tif',Butterworth_Lowpass_460_1)
cv2.waitKey(0)

Butterworth_Lowpass_10_3 = Butterworth_LPF(Alphabet_Image_FFT, 10,3)       
cv2.imshow('Butterworth_Lowpass_10_3', abs(Butterworth_Lowpass_10_3))
cv2.imwrite('Butterworth_Lowpass_10_3.tif',Butterworth_Lowpass_10_3)
cv2.waitKey(0)

Butterworth_Lowpass_30_3 = Butterworth_LPF(Alphabet_Image_FFT, 30,3)       
cv2.imshow('Butterworth_Lowpass_30_3', abs(Butterworth_Lowpass_30_3))
cv2.imwrite('Butterworth_Lowpass_30_3.tif',Butterworth_Lowpass_30_3)
cv2.waitKey(0)

Butterworth_Lowpass_60_3 = Butterworth_LPF(Alphabet_Image_FFT, 60,3)       
cv2.imshow('Butterworth_Lowpass_60_3', abs(Butterworth_Lowpass_60_3))
cv2.imwrite('Butterworth_Lowpass_60_3.tif',Butterworth_Lowpass_60_3)
cv2.waitKey(0)

Butterworth_Lowpass_160_3 = Butterworth_LPF(Alphabet_Image_FFT, 160,3)       
cv2.imshow('Butterworth_Lowpass_160_3', abs(Butterworth_Lowpass_160_3))
cv2.imwrite('Butterworth_Lowpass_160_3.tif',Butterworth_Lowpass_160_3)
cv2.waitKey(0)

Butterworth_Lowpass_460_3 = Butterworth_LPF(Alphabet_Image_FFT, 460,3)       
cv2.imshow('Butterworth_Lowpass_460_3', abs(Butterworth_Lowpass_460_3))
cv2.imwrite('Butterworth_Lowpass_460_3.tif',Butterworth_Lowpass_460_3)
cv2.waitKey(0)


Butterworth_Lowpass_10_5 = Butterworth_LPF(Alphabet_Image_FFT, 10,5)       
cv2.imshow('Butterworth_Lowpass_10_5', abs(Butterworth_Lowpass_10_5))
cv2.imwrite('Butterworth_Lowpass_10_5.tif',Butterworth_Lowpass_10_5)
cv2.waitKey(0)

Butterworth_Lowpass_30_5 = Butterworth_LPF(Alphabet_Image_FFT, 30,5)       
cv2.imshow('Butterworth_Lowpass_30_5', abs(Butterworth_Lowpass_30_5))
cv2.imwrite('Butterworth_Lowpass_30_5.tif',Butterworth_Lowpass_30_5)
cv2.waitKey(0)

Butterworth_Lowpass_60_5 = Butterworth_LPF(Alphabet_Image_FFT, 60,5)       
cv2.imshow('Butterworth_Lowpass_60_5', abs(Butterworth_Lowpass_60_5))
cv2.imwrite('Butterworth_Lowpass_60_5.tif',Butterworth_Lowpass_60_5)
cv2.waitKey(0)

Butterworth_Lowpass_160_5 = Butterworth_LPF(Alphabet_Image_FFT, 160,5)       
cv2.imshow('Butterworth_Lowpass_160_5', abs(Butterworth_Lowpass_160_5))
cv2.imwrite('Butterworth_Lowpass_160_5.tif',Butterworth_Lowpass_160_5)
cv2.waitKey(0)

Butterworth_Lowpass_460_5 = Butterworth_LPF(Alphabet_Image_FFT, 460,5)       
cv2.imshow('Butterworth_Lowpass_460_5', abs(Butterworth_Lowpass_460_5))
cv2.imwrite('Butterworth_Lowpass_460_5.tif',Butterworth_Lowpass_460_5)
cv2.waitKey(0)

