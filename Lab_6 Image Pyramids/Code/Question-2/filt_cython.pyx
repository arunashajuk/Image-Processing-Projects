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

def gaussian(float[:, :] im, double sigma):
    cdef int height = im.shape[0]  # cdef int tells Cython that this variable should be converted to a C int
    cdef int width = im.shape[1]   # 

    # cdef double[:, :, :] to store this as a 3D array of doubles
    cdef double[:, :] img_filtered = np.zeros([height, width])

    # A Gaussian has infinite support, but most of it's mass lies within
    # three standard deviations of the mean. The standard deviation is
    # the square of the variance, sigma.
    cdef int n = np.int(sqrt(sigma) * 3)

    cdef int p_y, p_x, i, j, q_y, q_x

    cdef double g, gpr
    cdef double w = 0

    # The rest of the code is similar, only now we have to explicitly assign the r, g, and b channels
    for p_y in range(height):
        for p_x in range(width):
            gpr = 0            
            w = 0
            for i in range(-n, n):
                for j in range(-n, n):
                    q_y = max([0, min([height - 1, p_y + i])])
                    q_x = max([0, min([width - 1, p_x + j])])
                    g = exp( -((q_x - p_x)**2 + (q_y - p_y)**2) / (2 * sigma**2) )
                                            
                    gpr += g * im[q_y, q_x]
                    
                    w += g
                    
            img_filtered[p_y, p_x] = gpr / (w + 1e-5)
            
    return img_filtered

