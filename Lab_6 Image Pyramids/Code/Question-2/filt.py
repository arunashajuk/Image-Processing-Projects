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
              gp = 0
              w = 0
  
              # Iterate over kernel locations to define pixel q
              for i in range(-n, n):
                  for j in range(-n, n):
                      # Make sure no index goes out of bounds of the image
                      q_y = np.max([0, np.min([height - 1, p_y + i])])
                      q_x = np.max([0, np.min([width - 1, p_x + j])])
                      # Computer Gaussian filter weight at this filter pixel
                      g = np.exp( -((q_x - p_x)**2 + (q_y - p_y)**2) / (2 * sigma**2) )

                      # Accumulate filtered output
                      gp += g * im[p_y, p_x, :]
                      # Accumulate filter weight for later normalization, to maintain image brightness
                      w += g
              img_filtered[p_y, p_x, :] = gp / (w + np.finfo(np.float32).eps)

      return img_filtered
