"""
Perform edge detection for the given images with and without using inbuilt functions
and compare the results.

"""

from PIL import Image, ImageOps
import numpy as np
import cv2


def Edge_Filter(Image_Noisy, Mask):
    
       
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


Image_Cameraman = cv2.imread("Cameraman.png")
Image_Cameraman = cv2.cvtColor(Image_Cameraman, cv2.COLOR_BGR2GRAY)

Cameraman_Image_1 = Image.open("Cameraman.png")
Cameraman_gray =  ImageOps.grayscale(Cameraman_Image_1)

# Sobel Masks

Sobel_x =   [[-1,0,1],
             [-2,0,2],
             [-1,0,1]]

Sobel_y =   [[1,2,1],
             [0,0,0],
             [-1,-2,-1]]

Sobel_x_inbuilt = cv2.Sobel(Image_Cameraman,cv2.CV_8U,1,0,ksize=3)
cv2.imshow('Sobel_x_inbuilt',Sobel_x_inbuilt)
cv2.imwrite('Sobel_x_inbuilt.png',Sobel_x_inbuilt)
cv2.waitKey(0)

Sobel_x_custom_function = Edge_Filter(Cameraman_gray, Sobel_x)
Sobel_x_custom_function.show()
Sobel_x_custom_function.save('Sobel_x_custom_function.png')

Sobel_y_inbuilt = cv2.Sobel(Image_Cameraman,cv2.CV_8U,0,1,ksize=3)
cv2.imshow('Sobel_y_inbuilt',Sobel_y_inbuilt)
cv2.imwrite('Sobel_y_inbuilt.png',Sobel_y_inbuilt)
cv2.waitKey(0)

Sobel_y_custom_function = Edge_Filter(Cameraman_gray, Sobel_y)
Sobel_y_custom_function.show()
Sobel_y_custom_function.save('Sobel_y_custom_function.png')

#Prewitt Masks

Prewitt_y = [[1,1,1],
             [0,0,0],
             [-1,-1,-1]]

Prewitt_x = [[1,0,-1],
             [1,0,-1],
             [1,0,-1]]

Prewitt_x_inbuilt = cv2.filter2D(Image_Cameraman, -1, np.array(Prewitt_x))
cv2.imshow('Prewitt_x_inbuilt',Prewitt_x_inbuilt)
cv2.imwrite('Prewitt_x_inbuilt.png',Prewitt_x_inbuilt)
cv2.waitKey(0)

Prewitt_x_custom_function = Edge_Filter(Cameraman_gray, Prewitt_x)
Prewitt_x_custom_function.show()
Prewitt_x_custom_function.save('Prewitt_x_custom_function.png')


Prewitt_y_inbuilt = cv2.filter2D(Image_Cameraman, -1, np.array(Prewitt_y))
cv2.imshow('Prewitt_y_inbuilt',Prewitt_y_inbuilt)
cv2.imwrite('Prewitt_y_inbuilt.png',Prewitt_y_inbuilt)
cv2.waitKey(0)

Prewitt_y_custom_function = Edge_Filter(Cameraman_gray, Prewitt_y)
Prewitt_y_custom_function.show()
Prewitt_y_custom_function.save('Prewitt_y_custom_function.png')

