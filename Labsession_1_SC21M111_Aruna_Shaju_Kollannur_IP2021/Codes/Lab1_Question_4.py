'''Question 4 ) Create, plot and save the Image
(a) Fully White Image(HINT pixel values are 255)
(b) Fully black Image(HINT pixel values are 0)'''


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')

image1_rows = int(input('Enter the height of the image to be created\n'))
image1_columns = int(input('Enter the width of the image to be created\n'))

image_white = np.full((image1_rows, image1_columns),255)
image_black = np.full((image1_rows, image1_columns),0)

image_white = np.uint8(image_white)
image_black = np.uint8(image_black)

image_white = Image.fromarray(image_white)
image_black = Image.fromarray(image_black)

fig = plt.figure()

fig.add_subplot(2,1,1)
plt.imshow(image_white, cmap= plt.get_cmap('gray'),vmin=0,vmax=255)


fig.add_subplot(2,1,2)
plt.imshow(image_black,  cmap= plt.get_cmap('gray'),vmin=0,vmax=255)


White_image = image_white.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\White_Image.jpeg")
Black_image = image_black.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\Black_Image.jpeg")