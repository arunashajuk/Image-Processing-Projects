import cv2
from matplotlib import pyplot as plt
from pywt import dwt2 , idwt2

img = cv2 . imread ("Cameraman.png",0)

cA , (cH , cV , cD ) = dwt2 ( img , 'db8')


plt . figure ()
plt . imshow (cA , cmap = "gray")
plt . title (" db8 coefficient cA")

plt . figure ()
plt . imshow (cH , cmap = "gray")
plt . title (" db8 coefficient cH")

plt . figure ()
plt . imshow (cV , cmap = "gray")
plt . title (" db8 coefficient cV")

plt . figure ()
plt . imshow (cD , cmap = "gray")
plt . title (" db8 coefficient cD")

plt . figure ()
plt . imshow ( img , cmap = "gray")
plt . title (" Original Image ")

recimg = idwt2 (( cA , (cH , cV , cD )) , 'db8')

plt . figure ()
plt . imshow ( recimg , cmap = "gray")
plt . title (" Reconstructed Image ")

