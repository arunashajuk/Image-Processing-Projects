' Wiener Filtering '

from PIL import Image, ImageOps
from scipy.signal.signaltools import wiener
import matplotlib.pyplot as plt
from Inverse_Filtering import Image_Original 
import numpy as np

Cameraman_Image = Image.open("Cameraman.png")
Cameraman_gray =  ImageOps.grayscale(Cameraman_Image)


img = Cameraman_gray 
filtered_img = wiener(img, (5, 5))  #Filter the image
f, (plot1, plot2) = plt.subplots(1, 2)

mean_square_error_orig_recovered = np.square(np.subtract(Image_Original,filtered_img)).mean()

print(f'The Mean Squared error between original and recovered image is {mean_square_error_orig_recovered}')

plot1.imshow(img)
plot2.imshow(filtered_img)
plt.show()