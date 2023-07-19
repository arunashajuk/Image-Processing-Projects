"""
Implement the unsharp masking algorithm
"""

from PIL import Image, ImageOps
import numpy as np


            
    
Cameraman_Image = Image.open("Cameraman.png")
Cameraman_gray =  ImageOps.grayscale(Cameraman_Image)

Factor = 3
Blur_Mask = np.full((Factor, Factor),(1/(Factor**2)))


height, width = Cameraman_gray.size
size = len(Blur_Mask)
pad = int((size-1)/2)

Image_copy_array = np.asarray(Cameraman_gray)

#Converting image to array
Pad_image = np.pad(np.array(Image_copy_array), ((pad,pad), (pad, pad)), 'constant')

# Creating a matrix with zeros to store convolution and correlation results

height_p = height + 2*pad
width_p = width + 2*pad

Corr_Image = np.full((height_p, width_p),0)

# Correlation

for i in range(pad,height-pad):
    for j in range(pad,width- pad):
        submatrix = Pad_image[i-pad:i+pad+1,j-pad:j+pad+1]  
        
        
        submatrix_mask_multipy_corr = np.multiply(submatrix , Blur_Mask)
        
        
        
        sum_elements_corr = list(map(sum, submatrix_mask_multipy_corr))
        Corr_Image[i,j] = sum(sum_elements_corr)

# Blurred Image
Corr_Image_cropped = Corr_Image[pad:height_p -pad,pad:width_p-pad]

# Blurred Image subtracted from original image
OG_subtract_blur = Image_copy_array - Corr_Image_cropped

# Unsharp mask added to original image

OG_plus_Edge_Mask = Image_copy_array + OG_subtract_blur

Corr_Image_cropped = np.clip(Corr_Image_cropped, 0, 255)
Corr_Image_cropped = Corr_Image_cropped.astype('uint8')
Blurred_Image = Image.fromarray(Corr_Image_cropped)

OG_subtract_blur = np.clip(OG_subtract_blur, 0, 255)
OG_subtract_blur = OG_subtract_blur.astype('uint8')
Blur_Subtracted_Image = Image.fromarray(OG_subtract_blur)

OG_plus_Edge_Mask = np.clip(OG_plus_Edge_Mask, 0, 255)
OG_plus_Edge_Mask = OG_plus_Edge_Mask.astype('uint8')
Unsharp_Image = Image.fromarray(OG_plus_Edge_Mask)


Blurred_Image.show()
Blurred_Image.save('Blurred_Image.png')

Blur_Subtracted_Image.show()
Blur_Subtracted_Image.save('Blur_Subtracted_Image.png')

Unsharp_Image.show()
Unsharp_Image.save('Unsharp_Image.png')







