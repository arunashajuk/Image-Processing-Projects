'''Implement a program for image convolution and correlation using a square
convolution mask of any odd size.(3, 5, etc.).'''

from PIL import Image, ImageOps
import numpy as np

Cameraman_Image = Image.open("Cameraman.png")
Cameraman_gray =  ImageOps.grayscale(Cameraman_Image)

Image_copy = Cameraman_gray.copy()
Image_DCT =  np.array(Cameraman_gray.copy())
Image_Reconstructed =  np.array(Cameraman_gray.copy())


height, width = Cameraman_gray.size

L = 8

C = np.zeros((L,L))
for k in range(L):
    for n in range(L):
        if k == 0:
            C[k,n] = np.sqrt(1/L)
        else:
            C[k,n] = np.sqrt(2/L)*np.cos((np.pi*k*(1/2+n))/L)
       
for i in range(0,height - L + 1,L):
    for j in range(0,width -L+ 1, L):
        
        submatrix = np.array(Image_copy)[i:i+L,j:j+L];
        temp = C.dot(submatrix)        
        temp1 = temp.dot(C.transpose())           
       
        Image_DCT[i:i+L,j:j+L] = temp1
 
         
for i in range(0,height - L + 1,L):
    for j in range(0,width -L+ 1, L):
        
        submatrix = np.array(Image_DCT)[i:i+L,j:j+L];
        temp = (C.transpose()).dot(submatrix)        
        temp1 = temp.dot(C)         
       
        Image_Reconstructed[i:i+L,j:j+L] = temp1

print(Image_Reconstructed)        

Image_DCT = np.clip(Image_DCT, 0, 255)
Image_DCT = Image_DCT.astype('uint8')
Image_DCT = Image.fromarray(Image_DCT)
Image_DCT.show()


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        