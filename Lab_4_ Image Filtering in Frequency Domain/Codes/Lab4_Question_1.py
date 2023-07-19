"""
Display the power spectrum of ’alphabet.tif ’ and compute the amount of
power enclosed within radii of 10, 30, 60, 160, and 460 pixels with respect to
the full-size spectrum.

"""
import numpy as np
import cv2
import math

import matplotlib.pyplot as plt

 
def Ideal_LPF_Filter(Image,cutoff):
    height, width = Image.shape
    
    Ideal_LPF = np.full((height, width),0)
    
    # Creating the Ideal Low Pass Filter Mask
    
    for i in range(height):
        for j in range(width):
             d = math.sqrt((i-int(height)/2)**2 + (j-int(width)/2)**2) 
             if (d <= cutoff):
                 Ideal_LPF[i,j] = 1
       
    Spectrum_covered = Ideal_LPF*Image
    return Spectrum_covered

def Total_Power(Image):
    height, width = Image.shape
    power_image = 0
    
    for i in range(height):
        for j in range(width):
           power_image = power_image + (abs(Image[i,j])**2)
           
    return power_image

def Power_Spectrum(Image):
    height, width = Image.shape
    
    Power_Spectrum_array = []
    
    for radius in range(int(height/2)):
        power_radius_unit = 0;
        
        for i in range(int(height/2) + radius, int(height/2)+ radius +1):
            for j in range(int(width/2) + radius, int(width/2)+ radius + 1):
               power_radius_unit = power_radius_unit + (abs(Image[i,j])**2)
               
        Power_Spectrum_array.append(power_radius_unit)   
        
    Power_Spectrum_array = Power_Spectrum_array/(np.median(Power_Spectrum_array))
        
    return Power_Spectrum_array 
    
def Power_Contained(Image, radius, Total_Power_image):
    height, width = Image.shape
    power_radius = 0
    
    for i in range(height):
        for j in range(width):
             d = math.sqrt((i-int(height)/2)**2 + (j-int(width)/2)**2) 
             if (d <= radius):            
                 power_radius = power_radius + (abs(Image[i,j])**2)
                
    alpha = (power_radius/Total_Power_image)*100
    
    return alpha

                
Alphabet_Image = cv2.imread("alphabet.tif", 0)
height, width = Alphabet_Image.shape

# Mirror Padding
#Alphabet_pad = np.pad(np.array(Alphabet_Image), ((int(height/2),int(height/2)),(int(width/2),int(width/2))),'symmetric')

# Zero Padding
Alphabet_pad = np.pad(np.array(Alphabet_Image), ((int(height/2),int(height/2)),(int(width/2),int(width/2))),'constant')

Alphabet_pad_centre = np.full((2*height, 2*width),0)

# Centering
for i in range(height*2):
    for j in range(width*2):
        
        Alphabet_pad_centre[i,j] = Alphabet_pad[i,j]*((-1)**(i+j))     

Alphabet_Image_FFT = np.fft.fft2(Alphabet_pad_centre)

Power_Spectrum_Image = Power_Spectrum(Alphabet_Image_FFT)

fig, ax = plt.subplots(figsize =(7, 5))
ax.hist(Power_Spectrum_Image , bins = range(len(Power_Spectrum_Image )))
# Show plot
plt.show()

Total_Power_Alphabet_Pad = Total_Power(Alphabet_Image_FFT)
         

radius_10 = Power_Contained(Alphabet_Image_FFT, 10 , Total_Power_Alphabet_Pad)
power_spectrum_10 = Ideal_LPF_Filter(Alphabet_Image_FFT, 10)
print(f' Power containd in 10 pixel radius is = {radius_10} %')
    
radius_30 = Power_Contained(Alphabet_Image_FFT, 30 , Total_Power_Alphabet_Pad)
power_spectrum_30 = Ideal_LPF_Filter(Alphabet_Image_FFT, 30)
print(f' Power containd in 30 pixel radius is = {radius_30} %')

radius_60 = Power_Contained(Alphabet_Image_FFT, 60 , Total_Power_Alphabet_Pad)
power_spectrum_60 = Ideal_LPF_Filter(Alphabet_Image_FFT, 60)
print(f' Power containd in 60 pixel radius is = {radius_60} %')

radius_160 = Power_Contained(Alphabet_Image_FFT, 160 , Total_Power_Alphabet_Pad)
power_spectrum_160 = Ideal_LPF_Filter(Alphabet_Image_FFT, 160)
print(f' Power containd in 160 pixel radius is = {radius_160} %')

radius_460 = Power_Contained(Alphabet_Image_FFT, 460 , Total_Power_Alphabet_Pad)
power_spectrum_460 = Ideal_LPF_Filter(Alphabet_Image_FFT, 460)
print(f' Power containd in 460 pixel radius is = {radius_460} %')


plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(Alphabet_Image_FFT)), cmap='gray');

plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(power_spectrum_10)), cmap='gray');

plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(power_spectrum_30)), cmap='gray');

plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(power_spectrum_60)), cmap='gray');

plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(power_spectrum_160)), cmap='gray');

plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(power_spectrum_460)), cmap='gray');




