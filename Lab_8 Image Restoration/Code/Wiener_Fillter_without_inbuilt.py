
import numpy as np
from numpy.fft import fft2, ifft2
from scipy.signal import gaussian
import cv2
#from Inverse_Filtering import Image_Original  

def wiener_filter(img, kernel, K):
	kernel /= np.sum(kernel)
	img_copy = np.copy(img)
	img_copy = fft2(img_copy)
	kernel = fft2(kernel, s = img.shape)
	kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
	img_copy = img_copy * kernel
	img_copy = np.abs(ifft2(img_copy))
	return img_copy

def gaussian_kernel(kernel_size = 3):
	h = gaussian(kernel_size, kernel_size / 3).reshape(kernel_size, 1)
	h = np.dot(h, h.transpose())
	h /= np.sum(h)
	return h

kernel = gaussian_kernel(5)
noisy_img = cv2.imread("Image_Blur_with_Noise.png", 0)


filtered_img = wiener_filter(noisy_img, kernel, K = 230)
'''mean_square_error_orig_recovered = np.square(np.subtract(Image_Original,filtered_img)).mean()

print(f'The Mean Squared error between original and recovered image is {mean_square_error_orig_recovered}')
'''
cv2.imshow('Image_Blur_with_Noise', abs(filtered_img))

cv2.waitKey(0)