import cv2
import numpy as np

canvas = np.zeros((300,300,3))

pts = np.array([[0,230], [250,90],[100,100]], np.int32)

pts = pts.reshape((-1,1,2))

cv2.polylines(canvas,[pts],True,(0,255,0),3)

cv2.imshow("shape show", canvas)
cv2.waitKey(5000)