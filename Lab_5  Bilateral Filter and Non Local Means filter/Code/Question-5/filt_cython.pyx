# Gaussian convolution applied at each pixel in an image (Cython version)
# Parameters:
#   im: Image to filter, provided as a numpy array
#   sigma:  The variance of the Gaussian (e.g., 1)
#

# Tell Cython to use the faster C libraries.
# If we add any additional math functions, we could also add their C versions here.
from libc.math cimport exp   
from libc.math cimport sqrt

import numpy as np

def non_local_mean(float[:, :] im, float[:, :] patch, double sigma):
    cdef int height = im.shape[0]  # cdef int tells Cython that this variable should be converted to a C int
    cdef int width = im.shape[1]   # 
        
    # cdef double[:, :, :] to store this as a 3D array of doubles
    cdef double[:, :] img_filtered = np.zeros([height, width])

    # A Gaussian has infinite support, but most of it's mass lies within
    # three standard deviations of the mean. The standard deviation is
    # the square of the variance, sigma.
    cdef int n = np.int(sqrt(sigma) * 3)

    cdef int p_y, p_x, i, j, q_y, q_x

    cdef double g1, g2r, g2g, g2b, gpr, gpg, gpb, gr, gg, gb
    cdef double w = 0
    

    # The rest of the code is similar, only now we have to explicitly assign the r, g, and b channels
    for p_y in range(int(n/2),height-int(n/2)):
          for p_x in range(int(n/2),width-int(n/2)):
              gpr = 0                        
              
              wr = 0
                           
  
              # Iterate over kernel locations to define pixel q
              for i in range(-int(n/2),int(n/2)+1):
                  for j in range(-int(n/2),int(n/2)+1):
                                                             
                      g2r = np.exp(-((im[(p_y + i),(p_x + j)]- patch[i,j])**2)/(2 * sigma**2))                                                                
                                            
                      # Accumulate filtered output
                      gpr += g2r * im[(p_y + i),(p_x + j)]                      
                      
                      # Accumulate filter weight for later normalization, to maintain image brightness
                      w += g2r                      
                    
              img_filtered[p_y, p_x] = im[p_y,p_x] + 0.5*(gpr / (w + 1e-5))             

    return img_filtered

