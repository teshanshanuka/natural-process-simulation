# -*- coding: utf-8 -*-
# Copyright (C) 2016 Universite de Geneve, Switzerland
# E-mail contact: sebastien.leclaire@etu.unige.ch
#
# The Parity Rule
#

from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm
import copy
import imageio

# Definition of functions
def readImage(string): # This function only work for monochrome BMP.
    image =  imageio.imread(string)
    image[image == 255] = 1
    image = image.astype(int)
    return image # Note that the image output is a numPy array of type "int".

# Main Program

# Program input, i.e. the name of the image "imageName" and the maximum number of iteration "maxIter"
imageName = 'image3.bmp'
maxIter   = 32

# Read the image and store it in the array "image"
image = readImage(imageName) # Note that "image" is a numPy array of type "int".
# Its element are obtained as image[i,j]
# Also, in the array "image" a white pixel correspond to an entry of 1 and a black pixel to an entry of 0.

# Get the shape of the image , i.e. the number of pixels horizontally and vertically.
# Note that the function shape return a type "tuple" (vertical_size,horizontal_size)
H, W = shape(image)

# Print to screen the initial image.
print(f'Image size: {image.shape}')
plt.clf()
plt.imshow(image, cmap=cm.gray)
plt.show()
plt.pause(0.1)

# Main loop
for it in range(1,maxIter+1):
    img_tmp = copy.copy(image)

    # You need to write here the core of the parity rule algorithm.
    # Altough not mandatory, you might need to use the array "imageCopy" and the tuple "imageSize".
    #
    for i in range(H):
        for j in range(W):
            l, r, t, b = img_tmp[(i-1)%H, j], img_tmp[(i+1)%H, j], img_tmp[i, (j-1)%W], img_tmp[i, (j+1)%W]
            image[i, j] = (l+r+t+b)%2

    # Print to screen the image after each iteration.
    # if it == maxIter:
    print('Image after',it,'iterations:')
    plt.clf()
    plt.imshow(image, cmap=cm.gray)
    plt.show()
    plt.pause(0.1)

# Print to screen the number of white pixels in the final image
print("The number of white pixels after",it,"iterations is: ", sum(image))
