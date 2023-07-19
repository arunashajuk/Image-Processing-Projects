# Gaussian convolution applied at each pixel in an image
  # Parameters:
  #   im: Image to filter, provided as a numpy array
  #   sigma:  The variance of the Gaussian (e.g., 1)
  #
import numpy as np
  
def gaussian(im, sigma):
      height, width, _ = im.shape
      img_filtered = np.zeros([height, width, 3])
  
      # Define filter size.
      # A Gaussian has infinite support, but most of it's mass lies within
      # three standard deviations of the mean. The standard deviation is
      # the square of the variance, sigma.
      n = np.int(np.sqrt(sigma) * 3)
  
      # Iterate over pixel locations p
      for p_y in range(height):
          for p_x in range(width):
              gpr = 0
              gpg = 0
              gpb = 0              
              
              wr = 0
              wg = 0
              wb = 0
              
  
              # Iterate over kernel locations to define pixel q
              for i in range(-n, n):
                  for j in range(-n, n):
                      # Make sure no index goes out of bounds of the image
                      q_y = np.max([0, np.min([height - 1, p_y + i])])
                      q_x = np.max([0, np.min([width - 1, p_x + j])])
                      # Computer Gaussian filter weight at this filter pixel
                      g1 = np.exp( -((q_x - p_x)**2 + (q_y - p_y)**2) / (2 * sigma**2) )
                      
                      g2r = np.exp(-((im[p_y,p_x,0]- im[q_y,q_x,0])**2)/(2 * sigma**2))
                      g2g = np.exp(-((im[p_y,p_x,1]- im[q_y,q_x,1])**2)/(2 * sigma**2))
                      g2b = np.exp(-((im[p_y,p_x,2]- im[q_y,q_x,2])**2)/(2 * sigma**2))
                      
                      gr = g1 *g2r
                      gg = g1 *g2g
                      gb = g1 *g2b
                      
                      # Accumulate filtered output
                      gpr += gr * im[p_y, p_x, 0]
                      gpg += gg * im[p_y, p_x, 1]
                      gpb += gb * im[p_y, p_x, 2]
                      
                      # Accumulate filter weight for later normalization, to maintain image brightness
                      wr += gr
                      wg += gg
                      wb += gb
                      
                      
              img_filtered[p_y, p_x, 0] = gpr / (wr + np.finfo(np.float32).eps)
              img_filtered[p_y, p_x, 1] = gpg / (wg + np.finfo(np.float32).eps)
              img_filtered[p_y, p_x, 2] = gpb / (wb + np.finfo(np.float32).eps)

      return img_filtered
