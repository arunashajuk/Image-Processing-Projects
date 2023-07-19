
import numpy as np
import cv2
import matplotlib.pyplot as plt
from Lab6_Question_1a import interpolate, handle_img_padding, create_gaussian_laplacian_pyramids, preprocess_odd_images

def plot_input(img, title):
    plt.imshow(img, cmap = 'gray')
    plt.title(title), plt.xticks([]), plt.yticks([])
    plt.show()

def min_sqr_err(mat1, mat2):
    min_sq = 0
    M, N = mat1.shape[:2]
    for i in range(M):
        for j in range(N):
            min_sq += np.square(mat1[i][j] - mat2[i][j])
    return min_sq

def reconstruct_original_img(G, L):
    reconstructed_images = []
    for i in range(len(G)-1 , 0, -1):
        expanded_img = interpolate(G[i])
        if expanded_img.shape[:2]!= L[i-1].shape[:2]:
            resized_img = handle_img_padding(L[i-1], expanded_img)
        reconstructed_images.append(resized_img + L[i-1])
        
    return reconstructed_images

original_img = cv2.imread('./Lenna.jpg', 0)
plot_input(original_img, 'Level0')
original_img = preprocess_odd_images(original_img)   

pyramid_levels = 6  

gaussian_pyramid, laplacian_pyramid = create_gaussian_laplacian_pyramids(original_img, pyramid_levels)


reconstructed_images = reconstruct_original_img(gaussian_pyramid, laplacian_pyramid)
final_image = reconstructed_images[-1]
plot_input(original_img, 'Original Image')
plot_input(final_image, 'Reconstructed Image')

print ("Minimum Squared Error (MSE) : ", min_sqr_err(original_img, final_image))

