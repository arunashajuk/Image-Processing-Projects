import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy . linalg import hadamard
import math

img = cv2 . imread ("Cameraman.png",0)

l= np.ceil (math.log ( img . shape [0] ,2)) 
m= np . ceil ( math . log ( img . shape [1] ,2) ) ;
img1 = cv2 . resize ( img , [ int ( pow (2 , max (l , m))) ,int( pow (2 , max(l ,m) )) ])
M , N = img1 . shape [:2]
H = hadamard (M )
print (H)
txmed = np . dot ( np . dot (H , img1 ) , np . transpose (H))
print ( txmed )

plt.figure()
plt . imshow ( img1 , cmap ="gray")
plt . title ('Original Image')

txmednor = np . real ( txmed ) / np . max ( np . real ( txmed ))

plt.figure()
plt . imshow ( np . log (1+( np . abs ( txmednor ))) , cmap ="gray")
plt . title ('Hadamard Transform Image')


inv_img = np . dot ( np . dot ( np . linalg . inv (H) , txmed ) , np . linalg . inv (H) )

plt.figure()
plt . imshow ( inv_img , cmap ="gray")
plt . title ('Reconstructed Image')
plt . show ()

