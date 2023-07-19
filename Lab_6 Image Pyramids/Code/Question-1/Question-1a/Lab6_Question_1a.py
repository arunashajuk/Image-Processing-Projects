
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Image size changed while kernel size kept constant

# 3x3 Gaussian kernel
gaussian_kernel = (1.0/16)*np.array([[1, 2, 1],[2,4,2],[1,2,1]])


# Odd size images converted into even size images to enable ease in downsampling at every pyramid level
def preprocess_odd_images(img):
    M, N = img.shape[:2]
    if M % 2 == 1 and N % 2 == 1:
        return img[1:][1:] # If both height and width odd, crop 1st row and column ( index 0)
    elif M%2 == 1:
        return img[1:][:]
    elif N%2 == 1:
        return img[:][1:]
    else:
        return img # no change if image height and width is even

def convolve(f, g): # f is image and g is kernel
    # Height and width of image and kernel
    f_height = f.shape[0]
    f_width = f.shape[1]
    g_height = g.shape[0]
    g_width = g.shape[1]
    
    g_height_mid = g_height // 2
    g_width_mid = g_width // 2
    
    # convolved image size made to incorporate zero padding size
    xmax = f_height + 2*g_height_mid
    ymax = f_width + 2*g_width_mid
    
    # Allocate result image.
    h = np.zeros([xmax, ymax], dtype=f.dtype)
    # Do convolution
    for x in range(xmax):
        for y in range(ymax):
            # Calculate pixel value for h at (x,y). Sum one component
            # for each pixel (s, t) of the filter g.
            s_from = max(g_height_mid - x, -g_height_mid)
            s_to = min((xmax - x) - g_height_mid, g_height_mid + 1)
            
            t_from = max(g_width_mid - y, -g_width_mid)
            t_to = min((ymax - y) - g_width_mid, g_width_mid + 1)
            
            value = 0
            for s in range(s_from, s_to):
                for t in range(t_from, t_to):
                    v = x - g_height_mid + s
                    w = y - g_width_mid + t
                    value += g[g_height_mid - s, g_width_mid - t] * f[v, w]
            h[x, y] = value
    return h

def interpolate(image):
    # Upsampling gaussian blur images for Laplacian pyramid
    
    image_up = np.zeros((2*image.shape[0], 2*image.shape[1]))
    # Inserting zeros at alternate positions forinterpolating by factor 2
    image_up[::2, ::2] = image
    # 4 multiplied with actual kernel as equvalent weight will be reduced due to convolving
    # with upsampled image containing alternate zeroes
    return convolve(image_up, 4*gaussian_kernel)


def gaussian_pyramid(image):
    # Convolution with gaussian blur
    image_blur = convolve(image, gaussian_kernel)
    # image downsampled by factor for next level
    return image_blur[::2, ::2]

def plot_input(img, title):
    plt.imshow(img, cmap = 'gray')
    plt.title(title), plt.xticks([]), plt.yticks([])
    plt.show()


def handle_img_padding(img1, img2):
    # height and width of both images
    M1, N1 = img1.shape[:2]
    M2, N2 = img2.shape[:2]
    padding_x = int(np.abs(M2 - M1)/2)
    padding_y = int(np.abs(N2 - N1)/2)
    img2 = img2[padding_x:M1+padding_x, padding_y: N1+padding_y]
    return img2

def create_gaussian_laplacian_pyramids(image, level):
    G = [image]
    L = []
    while level > 0:
        level -= 1
        image_blur = gaussian_pyramid(image)
        G.append(image_blur)
        expanded_img = interpolate(image_blur)
        if image.shape[:2] != expanded_img.shape[:2]:
            expanded_img = handle_img_padding(image, expanded_img)
        laplacian = image - expanded_img
        L.append(laplacian)
        image = image_blur
    return G, L


original_img = cv2.imread('./Lenna.jpg', 0)
plot_input(original_img, 'Level0')
original_img = preprocess_odd_images(original_img)
M,N = original_img.shape[:2]

pyramid_levels = 6     # 6 Gaussian Levels, inclusive of original image, lead to 5 Laplacian levels.     

gaussian_pyramid, laplacian_pyramid = create_gaussian_laplacian_pyramids(original_img, pyramid_levels)

for i in range(len(laplacian_pyramid)-1, 0, -1):
        plot_input(laplacian_pyramid[i], 'Laplacian Pyramid - Level '+ str(i))

for i in range(len(gaussian_pyramid)-1, 0, -1):
        plot_input(gaussian_pyramid[i], 'Gaussian Pyramid - Level '+ str(i-1))



