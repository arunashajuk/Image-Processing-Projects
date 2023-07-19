# Gaussian convolution applied at each pixel in an image
  # Parameters:
  #   im: Image to filter, provided as a numpy array
  #   sigma:  The variance of the Gaussian (e.g., 1)
  #
import numpy as np
  
def non_local_mean(im, patch, sigma):
      height, width, _ = im.shape
      img_filtered = np.zeros([height, width, 3])
  
      # Define filter size.
      # A Gaussian has infinite support, but most of it's mass lies within
      # three standard deviations of the mean. The standard deviation is
      # the square of the variance, sigma.
      n = np.int(np.sqrt(sigma) * 3)
  
      # Iterate over pixel locations p
      for p_y in range(n,height-n):
          for p_x in range(n,width-n):
              gpr = 0
              gpg = 0
              gpb = 0              
              
              wr = 0
              wg = 0
              wb = 0
              
  
              # Iterate over kernel locations to define pixel q
              for i in range(2*n):
                  for j in range(2*n):
                                                                  
                      g2r = np.exp(-((im[(p_y + i),(p_x + j),0]- patch[i,j,0])**2)/(2 * sigma**2))
                      g2g = np.exp(-((im[(p_y + i),(p_x + j),1]- patch[i,j,1])**2)/(2 * sigma**2))
                      g2b = np.exp(-((im[(p_y + i),(p_x + j),2]- patch[i,j,2])**2)/(2 * sigma**2))                                           
                                            
                      # Accumulate filtered output
                      gpr += g2r * im[(p_y + i),(p_x + j),0]
                      gpg += g2g * im[(p_y + i),(p_x + j),1]
                      gpb += g2b * im[(p_y + i),(p_x + j),2]
                      
                      # Accumulate filter weight for later normalization, to maintain image brightness
                      wr += g2r
                      wg += g2g
                      wb += g2b                      
                      
              img_filtered[p_y, p_x, 0] = gpr / (wr + np.finfo(np.float32).eps)
              img_filtered[p_y, p_x, 1] = gpg / (wg + np.finfo(np.float32).eps)
              img_filtered[p_y, p_x, 2] = gpb / (wb + np.finfo(np.float32).eps)

      return img_filtered
