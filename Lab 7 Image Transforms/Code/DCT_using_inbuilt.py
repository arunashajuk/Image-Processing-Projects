import cv2
import numpy as np

# Blocksize of DCT matrix used, thus image divided into 8*8 sizes to 
#perform transformation

B = 8 

Image_Cameraman = cv2 . imread ( "Cameraman.png",0)
h ,w= np . array ( Image_Cameraman . shape [:2]) /B * B
h= int (h );w= int (w) ;
Image_Cameraman = Image_Cameraman [:h ,: w]

Vertical_blocks =int (h/B)
Horizontal_blocks =int (w/B)
Image_Temp = np . zeros ((h ,w) , np . float32 )
Image_DCT = np . zeros ((h ,w ) , np . float32 )
Image_Temp [:h , : w] = Image_Cameraman

# Applying DCT Blockwise

for row in range ( Vertical_blocks ):
 for col in range ( Horizontal_blocks ):
   Current_Block = cv2 . dct ( Image_Temp [ row *B :( row +1) *B , col *B :( col +1) *B ])
   Image_DCT [ row *B :( row +1) *B , col *B :( col +1) *B ]= Current_Block
  
  
cv2.imwrite ('DCT Transformed.png', Image_DCT )
back0 = np . zeros ((h ,w ) , np . float32 )

# Applying IDCT Blockwise to get reconstructed image

for row in range ( Vertical_blocks ):
  for col in range ( Horizontal_blocks ):
    Current_Block = cv2 . idct ( Image_DCT [ row *B :( row +1) *B , col *B :( col +1) * B ])
    back0 [ row *B :( row +1) *B , col *B :( col +1) *B ]= Current_Block
    
cv2.imwrite("DCT_Reconstructed_Image.jpg", back0 )



