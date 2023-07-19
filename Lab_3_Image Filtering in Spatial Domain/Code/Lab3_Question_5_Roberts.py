"""
Perform edge detection for the given images with and without using inbuilt functions
and compare the results.

"""

from PIL import Image, ImageOps
import numpy as np
import cv2
from skimage import filters

def Roberts_Filter(Image_Noisy, Mask):
    
       
    paddy = int(len(Mask)/2)
    height, width = Image_Noisy.size
    
    Image_copy_array = np.asarray(Image_Noisy)

    #Converting image to array
    Pad_image = np.pad(np.array(Image_copy_array), ((0,paddy), (0, paddy)), 'constant')

    # Creating a matrix with zeros to store convolution and correlation results

    height_p = height + paddy
    width_p = width + paddy
    
    Corr_Image = np.full((height_p, width_p),0)

    # Correlation  of Image with Even Order Mask

    for i in range(0,height_p-paddy):
        for j in range(0,width_p- paddy):
            submatrix = Pad_image[i:i+paddy+1,j:j+paddy+1]
            
            
            submatrix_mask_multipy_corr = np.multiply(submatrix , Mask)
            
                    
            sum_elements_corr = list(map(sum, submatrix_mask_multipy_corr))
            Corr_Image[i,j] = sum(sum_elements_corr)
            
    Corr_Image_cropped = Corr_Image[0:height_p -paddy,0:width_p-paddy]
    Corr_Image_cropped = np.clip(Corr_Image_cropped, 0, 255)
    Corr_Image_cropped = Corr_Image_cropped.astype('uint8')

    
    Correlated_Image = Image.fromarray(Corr_Image_cropped)
    
    return Correlated_Image


Image_Cameraman = cv2.imread("Cameraman.png")
Image_Cameraman = cv2.cvtColor(Image_Cameraman, cv2.COLOR_BGR2GRAY)

Cameraman_Image_1 = Image.open("Cameraman.png")
Cameraman_gray =  ImageOps.grayscale(Cameraman_Image_1)


#Roberts Mask

Roberts_x = [[1,0],
             [0,-1]]

Roberts_y = [[0,1],
             [-1,-0]]

Roberts_x_inbuilt = filters.roberts_neg_diag(Image_Cameraman)
cv2.imshow('Roberts_x_inbuilt',Roberts_x_inbuilt)
cv2.imwrite('Roberts_x_inbuilt.png',Roberts_x_inbuilt)
cv2.waitKey(0)

Roberts_x_custom_function = Roberts_Filter(Cameraman_gray, Roberts_x)
Roberts_x_custom_function.show()
Roberts_x_custom_function.save('Roberts_x_custom_function.png')


Roberts_y_inbuilt = filters.roberts_pos_diag(Image_Cameraman)
cv2.imshow('Roberts_y_inbuilt',Roberts_y_inbuilt)
cv2.imwrite('Roberts_y_inbuilt.png',Roberts_y_inbuilt)
cv2.waitKey(0)

Roberts_y_custom_function = Roberts_Filter(Cameraman_gray, Roberts_y)
Roberts_y_custom_function.show()
Roberts_y_custom_function.save('Roberts_y_custom_function.png')