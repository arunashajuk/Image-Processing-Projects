'''Question 2)  Read, display and save the ”lenna.jpg” image to another format. Also display the image
format, size, mode and information of the original image using built in commands.'''


from PIL import Image
from PIL.ExifTags import TAGS

# Reading an image
imag_lenna = Image.open(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\Lenna.jpeg")

#Displaying the read image
imag_lenna.show()

#Saving the image as a pdf
lenna_pdf = imag_lenna.save(r"C:\Users\Aruna Shaju K\Documents\Image-Processing-Lab-Images\Lenna_pdf.pdf")

print(f"The format of Lenna image is {imag_lenna.format}")
print(f"The size of Lenna image is {imag_lenna.size}")
print(f"The mode of Lenna image is {imag_lenna.mode}")

# Extracting metadata of image and displaying it

exifdata = imag_lenna.getexif()
# Iterating over all EXIF data fields

for tag_id in exifdata:
    
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
       
    try:
        if isinstance(data, bytes):
           data = data.decode()
    except :
        print()
    print(f"{tag:25}: {data}")
    