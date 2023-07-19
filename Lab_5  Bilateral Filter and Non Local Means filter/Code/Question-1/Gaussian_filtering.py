# Gaussian convolution applied at a pixel in an image
import numpy as np
from PIL import Image
import filt

img = np.array(Image.open('rubiks_cube.png'), dtype=np.float32)
img_filtered = np.asarray(filt.gaussian(img, 3))
img_filtered = np.clip(img_filtered, 0, 255)
Image.fromarray(img_filtered.astype(np.uint8)).show()
Image.fromarray(img_filtered.astype(np.uint8)).save('Gaussian-Intensity-Linear-Filtered.png')
