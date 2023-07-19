# Gaussian convolution applied at a pixel in an image
import numpy as np
from PIL import Image
import filt

img = np.array(Image.open('Lenna_gray.png'), dtype=np.float32)
height, width = img.shape

sigma = 1
n = int(np.sqrt(sigma) * 3)

#patch_compare = img[int(height/2):(int(height/2) + n), int(width/2):(int(width/2) + n)]

# Taking patch from top-left most corner
patch_compare = img[0:(n), 0:(n)]    
        
img_filtered = np.asarray(filt.non_local_mean(img,patch_compare,sigma))
img_filtered = np.clip(img_filtered, 0, 255)
Image.fromarray(img_filtered.astype(np.uint8)).show()
Image.fromarray(img_filtered.astype(np.uint8)).save('Non_Local_Mean.png')
Image.fromarray(patch_compare.astype(np.uint8)).save('patch.png')
