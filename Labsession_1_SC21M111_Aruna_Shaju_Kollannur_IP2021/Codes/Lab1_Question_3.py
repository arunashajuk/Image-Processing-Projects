# -*- coding: utf-8 -*-
"""
Question 3)  Familiarize the following basic commands in PIL:
(a) crop, paste
(b) split, merge
(c) resize, rotate, transform
(d) blend
(e) convert, copy
(f) getbands, getextrema, getpixel, putpixel
"""

from PIL import Image

Image_Cameraman = Image.open(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\Cameraman.png")
Image_Lenna = Image.open(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\Lenna.jpeg")

Image_Lenna_2 = Image.open(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\Lenna.jpeg")


width, height = Image_Cameraman.size
width_l, height_l = Image_Lenna.size

# a-1 ) Cropping the image from top-right pixel to bottom-left pixel position diagonally 
imag_crop = Image_Cameraman.crop((0, height/4, width/2, 3*height/4))
imag_crop.show()
imag_crop.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_crop.png")

# a-2 )Pasting cropped Cameraman image to Lenna image
Image.Image.paste(Image_Lenna, imag_crop, (20, 50))
Image_Lenna.show()
Image_Lenna.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_paste.png")

# b-1 ) splitting image into red blie and green intensity array 
imag_split  = Image.Image.split(Image_Lenna_2)
imag_split[0].show()
imag_split[0].save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_split_R.png")

imag_split[1].show()
imag_split[1].save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_split_G.png")

imag_split[2].show()
imag_split[2].save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_split_B.png")

# b-2 ) merging the image in the order RBG from split RGB intensity array
imag_merge = Image.merge( 'RGB', (imag_split[0], imag_split[2],imag_split[1]))
imag_merge.show()
imag_merge.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_merge.png")

# c- 1 ) resizing an image
imag_resize = Image_Cameraman.resize((width -100,height - 100))
imag_resize.show()
imag_resize.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_resize.png")

# c- 2 ) rotating an image
imag_rotate = Image_Cameraman.rotate(48)
imag_rotate.show()
imag_rotate.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_rotate.png")

# c- 3 ) tranforming  an image to its extent at top-left (0-10) to bottom right (width/4, height/4))
imag_transform = Image_Cameraman.transform((width - 100, height-200), Image.EXTENT, data =[10, 0, 10 + width_l // 4, height_l // 3 ])
imag_transform.show()
imag_transform.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_transform.png")

# d ) blending two images
blend_into_image = imag_transform.resize((width,height ))

blend_into_image.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\blend_into_image.png")
imag_blend = Image.blend(Image_Cameraman,blend_into_image, 25.0)

imag_blend.show()
imag_blend.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_blend.png")

#e-1) Converting an image to diether mode 1 (noise inclusion)
imag_convert = Image_Cameraman.convert("1")
imag_convert.show()
imag_convert.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_convert.png")

#e-2) Copying an image
imag_copy = Image_Cameraman.copy()
imag_copy.show()
imag_copy.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_copy.png")

#f-1) Printing the bands of an image
imag_band = Image_Cameraman.getbands()
print("The bands of image Cameraman are ", imag_band)

#f-2) Printing max and min pixel values of an image
imag_extremes = Image.Image.getextrema(Image_Cameraman)
print("The extreme(max and min) of image Cameraman are ", imag_extremes)

#f-3 ) Outputting pixel intensity at certain position
imag_getpixel = Image_Cameraman.getpixel((width//2, height//2))
print("The pixel intensity at ",(width//2, height//2),"are", imag_getpixel )

#f-4) Putting an range of pixels in an image

for i in range(height//4, height*3//4) :
    for j in range(width//4,width*3//4):
        imag_copy.putpixel((i,j),(200,125,300,255))
        
imag_copy.show()
imag_copy.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\imag_put_pixel.png")