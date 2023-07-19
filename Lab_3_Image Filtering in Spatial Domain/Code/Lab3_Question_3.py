# -*- coding: utf-8 -*-
"""
From the outputs obtained from question 2 i.e., noisy images, perform average filtering over the images and state which type of noise is best removed
using average filter.
Use 3 × 3, 5 × 5, 11 × 11 masks
"""
from PIL import Image, ImageOps
import numpy as np

def Avg_Filter(Image_Noisy, Factor):
    
    # Odd mask created with order Factor*Factor 
    
    Mask = np.full((Factor, Factor),(1/(Factor**2)))
    
    size = len(Mask)
    paddy = int((size-1)/2)
    height, width = Image_Noisy.size
    
    Image_copy_array = np.asarray(Image_Noisy)

    #Converting image to array
    Pad_image = np.pad(np.array(Image_copy_array), ((paddy,paddy), (paddy, paddy)), 'constant')

    # Creating a matrix with zeros to store convolution and correlation results

    height_p = height + 2*paddy
    width_p = width + 2*paddy
    
    Corr_Image = np.full((height_p, width_p),0)

    # Correlation

    for i in range(paddy,height_p-paddy):
        for j in range(paddy,width_p- paddy):
            submatrix = Pad_image[i-paddy:i+paddy+1,j-paddy:j+paddy+1]  
            
            
            submatrix_mask_multipy_corr = np.multiply(submatrix , Mask)
            
                    
            sum_elements_corr = list(map(sum, submatrix_mask_multipy_corr))
            Corr_Image[i,j] = sum(sum_elements_corr)
            
    Corr_Image_cropped = Corr_Image[paddy:height_p -paddy,paddy:width_p-paddy]  
    
    Corr_Image_cropped = np.clip(Corr_Image_cropped, 0, 255)
    Corr_Image_cropped = Corr_Image_cropped.astype('uint8')

    Correlated_Image = Image.fromarray(Corr_Image_cropped)
    return Correlated_Image


Noisy_Salt_and_Pepper = Image.open("Cameraman_Noise_Salt_and_Pepper.jpeg")
Noisy_Salt_and_Pepper =  ImageOps.grayscale(Noisy_Salt_and_Pepper)

Noisy_Speckle = Image.open("Cameraman_Noise_Speckle.jpeg")
Noisy_Speckle = ImageOps.grayscale(Noisy_Speckle)

Noisy_Gaussian = Image.open("Cameraman_Noise_Gaussian.jpeg")
Noisy_Gaussian =  ImageOps.grayscale(Noisy_Gaussian)

Noisy_Poisson = Image.open("Cameraman_Noise_Poisson.jpeg")
Noisy_Poisson = ImageOps.grayscale(Noisy_Poisson)

#Passing Noisy images through Averaging Filter

Noisy_Salt_and_Pepper_Avg_3 = Avg_Filter(Noisy_Salt_and_Pepper, 3)
Noisy_Salt_and_Pepper_Avg_3.show()
Noisy_Salt_and_Pepper_Avg_3.save('Noisy_Salt_and_Pepper_Avg_3.png')

Noisy_Salt_and_Pepper_Avg_5 = Avg_Filter(Noisy_Salt_and_Pepper, 5)
Noisy_Salt_and_Pepper_Avg_5.show()
Noisy_Salt_and_Pepper_Avg_5.save('Noisy_Salt_and_Pepper_Avg_5.png')

Noisy_Salt_and_Pepper_Avg_11 = Avg_Filter(Noisy_Salt_and_Pepper, 11)
Noisy_Salt_and_Pepper_Avg_11.show()
Noisy_Salt_and_Pepper_Avg_11.save('Noisy_Salt_and_Pepper_Avg_11.png')


Noisy_Speckle_Avg_3 = Avg_Filter(Noisy_Speckle, 3)
Noisy_Speckle_Avg_3.show()
Noisy_Speckle_Avg_3.save('Noisy_Speckle_Avg_3.png')

Noisy_Speckle_Avg_5 = Avg_Filter(Noisy_Speckle, 5)
Noisy_Speckle_Avg_5.show()
Noisy_Speckle_Avg_5.save('Noisy_Speckle_Avg_5.png')

Noisy_Speckle_Avg_11 = Avg_Filter(Noisy_Speckle, 11)
Noisy_Speckle_Avg_11.show()
Noisy_Speckle_Avg_11.save('Noisy_Speckle_Avg_11.png')


Noisy_Gaussian_Avg_3 = Avg_Filter(Noisy_Gaussian, 3)
Noisy_Gaussian_Avg_3.show()
Noisy_Gaussian_Avg_3.save('Noisy_Gaussian_Avg_3.png')

Noisy_Gaussian_Avg_5 = Avg_Filter(Noisy_Gaussian, 5)
Noisy_Gaussian_Avg_5.show()
Noisy_Gaussian_Avg_5.save('Noisy_Gaussian_Avg_5.png')

Noisy_Gaussian_Avg_11 = Avg_Filter(Noisy_Gaussian, 11)
Noisy_Gaussian_Avg_11.show()
Noisy_Gaussian_Avg_11.save('Noisy_Gaussian_Avg_11.png')


Noisy_Poisson_Avg_3 = Avg_Filter(Noisy_Poisson, 3)
Noisy_Poisson_Avg_3.show()
Noisy_Poisson_Avg_3.save('Noisy_Poisson_Avg_3.png')

Noisy_Poisson_Avg_5 = Avg_Filter(Noisy_Poisson, 5)
Noisy_Poisson_Avg_5.show()
Noisy_Poisson_Avg_5.save('Noisy_Poisson_Avg_5.png')

Noisy_Poisson_Avg_11 = Avg_Filter(Noisy_Poisson, 11)
Noisy_Poisson_Avg_11.show()
Noisy_Poisson_Avg_11.save('Noisy_Poisson_Avg_11.png')










