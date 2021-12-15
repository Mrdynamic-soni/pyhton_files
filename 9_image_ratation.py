import cv2
import numpy 

image = cv2.imread("D:\\projects\\opencv_projects\\pyhton_files\\imresize.jpg")
height, width = image.shape[:2]

matrix = cv2.getRotationMatrix2D((width/2,height/2),90,1)

rotated_image = cv2.warpAffine(image, matrix, (width,height))

cv2.imshow("rotated_image", rotated_image)
cv2.waitKey(3000)