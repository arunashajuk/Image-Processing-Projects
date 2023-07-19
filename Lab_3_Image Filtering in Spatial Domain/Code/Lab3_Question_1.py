'''Implement a program for image convolution and correlation using a square
convolution mask of any odd size.(3, 5, etc.).'''

from PIL import Image, ImageOps
import numpy as np

Cameraman_Image = Image.open("Cameraman.png")
Cameraman_gray =  ImageOps.grayscale(Cameraman_Image)

Image_copy = Cameraman_gray.copy()

height, width = Cameraman_gray.size

# Correlation mask used (size 3x3)

Corr_Mask = [[1,-1,-1],
             [1,2,-1],
             [1,1,1]]

       
# 180 degree flipped Convolution mask
Flip_Conv_Mask =  np.flipud(np.fliplr(Corr_Mask))

# Padding size 
size = len(Flip_Conv_Mask)
pad = int((size-1)/2)

# Padding image for convolution
Image_copy_array = np.asarray(Image_copy)

#Converting image to array
Pad_image = np.pad(np.array(Image_copy_array), ((pad,pad), (pad, pad)), 'constant')

# Creating a matrix with zeros to store convolution and correlation results

height_p = height + 2*pad
width_p = width + 2*pad
Conv_Image = np.full((height_p, width_p),0)
Corr_Image = np.full((height_p, width_p),0)

# Convolution and Correlation

for i in range(pad,height_p-pad):
    for j in range(pad,width_p- pad):
        submatrix = Pad_image[i-pad:i+pad+1,j-pad:j+pad+1]  
        
        submatrix_mask_multipy_conv = np.multiply(submatrix , Flip_Conv_Mask)
        submatrix_mask_multipy_corr = np.multiply(submatrix , Corr_Mask)
        
        sum_elements_conv = list(map(sum, submatrix_mask_multipy_conv))
        Conv_Image[i,j] = sum(sum_elements_conv)
        
        sum_elements_corr = list(map(sum, submatrix_mask_multipy_corr))
        Corr_Image[i,j] = sum(sum_elements_corr)

# Extract Convoulted image from padded zero Convoulted Image

Conv_Image_cropped = Conv_Image[pad:height_p -pad,pad:width_p-pad]
Corr_Image_cropped = Corr_Image[pad:height_p -pad,pad:width_p-pad]

# Saturate all pixel values greater than 255 to 255
Conv_Image_cropped = np.clip(Conv_Image_cropped, 0, 255)
Conv_Image_cropped = Conv_Image_cropped.astype('uint8')

Corr_Image_cropped = np.clip(Corr_Image_cropped, 0, 255)
Corr_Image_cropped = Corr_Image_cropped.astype('uint8')

# Converting array containing convolution results to image
Convoluted_Image = Image.fromarray(Conv_Image_cropped)
Correlated_Image = Image.fromarray(Corr_Image_cropped)

Convoluted_Image.show()
Convoluted_Image.save('Cameraman_Convoluted.png')       
        
Correlated_Image.show()
Correlated_Image.save('Cameraman_Correlated.png')       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        