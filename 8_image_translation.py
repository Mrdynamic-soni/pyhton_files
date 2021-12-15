# shifting image from one position to other is called image yranslation
#      |1 0 tx|   translational matrix
#  T = |0 1 ty|
     
import cv2 
import numpy

image = cv2.imread("D:\\projects\\opencv_projects\\pyhton_files\\imresize.jpg")
matrix = numpy.float32([[1,0,100],[0,1,100]])

translated_image = cv2.warpAffine(image,matrix,(image.shape[1]+100,image.shape[0]+100))

cv2.imshow('translated', translated_image)
cv2.waitKey(5000)