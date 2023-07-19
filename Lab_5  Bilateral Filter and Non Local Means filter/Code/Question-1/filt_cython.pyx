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

def gaussian(float[:, :, :] im, double sigma):
    cdef int height = im.shape[0]  # cdef int tells Cython that this variable should be converted to a C int
    cdef int width = im.shape[1]   # 

    # cdef double[:, :, :] to store this as a 3D array of doubles
    cdef double[:, :, :] img_filtered = np.zeros([height, width, 3])

    # A Gaussian has infinite support, but most of it's mass lies within
    # three standard deviations of the mean. The standard deviation is
    # the square of the variance, sigma.
    cdef int n = np.int(sqrt(sigma) * 3)

    cdef int p_y, p_x, i, j, q_y, q_x

    cdef double g1, g2r, g2g, g2b, gpr, gpg, gpb, gr, gg, gb
    cdef double wr = 0
    cdef double wg = 0
    cdef double wb = 0

    # The rest of the code is similar, only now we have to explicitly assign the r, g, and b channels
    for p_y in range(height):
        for p_x in range(width):
            gpr = 0
            gpg = 0
            gpb = 0
            
            wr= 0
            wb=0
            wg=0
            
            for i in range(-n, n):
                for j in range(-n, n):
                    q_y = max([0, min([height - 1, p_y + i])])
                    q_x = max([0, min([width - 1, p_x + j])])
                    
                    g1 = exp( -((q_x - p_x)**2 + (q_y - p_y)**2) / (2 * sigma**2) )
                    
                    g2r = abs(im[p_y,p_x,0]- im[q_y,q_x,0])
                    g2g = abs(im[p_y,p_x,1]- im[q_y,q_x,1])
                    g2b = abs(im[p_y,p_x,2]- im[q_y,q_x,2])                   
                    
                                        
                    gr = g1 *g2r;
                    gg = g1 *g2g;
                    gb = g1 *g2b;           
                     
                       
                    gpr += gr * im[q_y, q_x, 0]
                    gpg += gg * im[q_y, q_x, 1]
                    gpb += gb * im[q_y, q_x, 2]
                    
                    wr += gr
                    wg += gg
                    wb += gb
                    
            img_filtered[p_y, p_x, 0] = gpr / (wr + 1e-5)
            img_filtered[p_y, p_x, 1] = gpg / (wb + 1e-5)
            img_filtered[p_y, p_x, 2] = gpb / (wg + 1e-5)

    return img_filtered

