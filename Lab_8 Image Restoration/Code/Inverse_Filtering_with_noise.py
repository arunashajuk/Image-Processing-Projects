' Inverse Filtering with original image with noise'

import numpy as np
import cv2

import matplotlib.pyplot as plt



Image_Original = cv2.imread("Cameraman.png", 0)
Image_Blur = cv2.GaussianBlur(Image_Original, (5, 5), 0) + np.random.normal(0,10,(256,256))


Image_Original_Freq = np.fft.fft2(Image_Original)
Image_Blur_Freq = np.fft.fft2(Image_Blur)

H_SPF = Image_Blur_Freq/Image_Original_Freq
Inverse_H_SPF = 1/H_SPF

Inverse_Filtering_Output_Freq = Image_Blur_Freq*Inverse_H_SPF

Inverse_Filtering_Output = np.fft.ifft2(Inverse_Filtering_Output_Freq)

Inverse_Filtering_Output = np.clip(Inverse_Filtering_Output, 0, 255)
Inverse_Filtering_Output = Inverse_Filtering_Output.astype('uint8')



cv2.imshow('Image_Original', abs(Image_Original))
cv2.waitKey(0)

cv2.imshow('Image_Blur_with_noise', abs(Image_Blur))
cv2.imwrite('Image_Blur_with_noise.png',Image_Blur)
cv2.waitKey(0)

plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(H_SPF)), cmap='gray');

plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(Inverse_H_SPF)), cmap='gray');


cv2.imshow('Inverse_Filtering_Output_noise', abs(Inverse_Filtering_Output))
cv2.imwrite('Inverse_Filtering_Output_noise.png',Inverse_Filtering_Output)
cv2.waitKey(0)

mean_square_error_orig_blur = np.square(np.subtract(Image_Original,Image_Blur)).mean()
mean_square_error_orig_recovered = np.square(np.subtract(Image_Original,Inverse_Filtering_Output)).mean()

print(f'The Mean Squared error between original and blurred image is {mean_square_error_orig_blur}')
print(f'The Mean Squared error between original and recovered image is {mean_square_error_orig_recovered}')