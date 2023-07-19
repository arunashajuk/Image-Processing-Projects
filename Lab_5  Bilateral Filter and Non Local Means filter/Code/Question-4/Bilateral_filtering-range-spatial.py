# Gaussian convolution applied at a pixel in an image
import numpy as np
from PIL import Image
import filt

img = np.array(Image.open('Lenna_noisy.png'), dtype=np.float32)

range_sigma = [0.05,1,2,4,8]
spatial_sigma = [2,4,8,16,32]

for i in range_sigma:
    for j in spatial_sigma:
        
     img_filtered= np.asarray(filt.gaussian(img,i,j))
     img_filtered = np.clip(img_filtered, 0, 255)
     Image_filtered = Image.fromarray(img_filtered.astype(np.uint8))
     #Image_filtered.show()
     
     outfile = '%s%d%s%f.png' % ("Bilateral_Filter_Spatial_sigma_",j,"_Range_sigma_",i)
     Image_filtered.save(outfile)
