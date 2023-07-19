
import numpy as np
from PIL import Image
import filt
import cv2
import matplotlib.pyplot as plt

def min_sqr_err(mat1, mat2):
    min_sq = 0
    M, N = mat1.shape[:2]
    for i in range(M):
        for j in range(N):
            min_sq += np.square(mat1[i][j] - mat2[i][j])
    return min_sq

img = cv2.imread('Lenna.png', 0)
G = [img]
L = []
outfile = '%s.png' % ("Lenna")

for dev in range(1,6):
 p = np.array(Image.open(outfile), dtype=np.float32)
 
 img_filtered = np.asarray(filt.gaussian(p, dev))
 Image_gaussian_filtered = Image.fromarray(img_filtered.astype(np.uint8))
 # Gaussian Pyramid
 G.append(Image_gaussian_filtered)
 outfile = '%s%d.jpg' % ("Lenna_Gaussian_Pyramid",dev)
 Image_gaussian_filtered.save(outfile)
 # Laplacian Pyramid
 L.append(np.array(G[dev-1], dtype=np.float32) - np.array(G[dev], dtype=np.float32)) 
 
# Reconstruction
Reconstructed_Image = np.array(G[-1])

for dev in range(5):    
    Reconstructed_Image = Reconstructed_Image + L[dev]

Mean_square_error = min_sqr_err(img,Reconstructed_Image ) 
print(f'Mean square error is {Mean_square_error}')   
plt.imshow(Reconstructed_Image, cmap = 'gray')
 
 
 
 
 


