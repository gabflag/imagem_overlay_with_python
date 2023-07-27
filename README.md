# imagem_overlay_with_python

# Programming Language used:

    Python 3.11.2
    To start the program just run the file make_water_and_instagram_story.py
    
# About the program:
    
This is a program aimed at those who wish to automatically add a watermark to an image. Here you will find the necessary logic for that.
You will also find a way to identify if an image is in a 9:16 format.
This is not a program developed with common users in mind; reading and coding skills are necessary for its implementation.

# Solutions to possible problems

If you encounter any issues with JPEG images, modify the code in the 'overlay_image_default' function. This is a problem that usually occurs when working with JPEG images.

    new_image = Image.new("RGB", background.size, (0, 0, 0))

# More about the development

To avoid problems with images of different sizes, a resizing to 1080px was made, respecting the aspect ratio of the respective image.
Creating a watermark with a width of 1080px made it much easier to place it on the image.
There are two backgrounds available for images in the 9:16 format.

# Exemple:

