import numpy as np
import cv2
from numpy.lib.type_check import imag

image = np.zeros((500,500)) # creating array for image of size 500X500
# print(image)
image[:,:] = 100  #making image gray usng (0-255) values
image[100:200,100:200] = 255 # making a specific area black 

cv2.imwrite("numpy_img.jpg",image)

img = cv2.imread("numpy_img.jpg",1)
cv2.imshow("imag",img)