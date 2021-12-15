import cv2
import numpy as np 

canvas = np.zeros((500,500,3))

#drawing a line
cv2.line(canvas,(0,0),(250,300),(230,120,45),thickness=3,lineType= cv2.LINE_AA)

#drawing a circle 
cv2.circle(canvas,(250,250),30,(234,76,231),3)

#drawing a rectangle
cv2.rectangle(canvas,(10,30),(100,200),(230,67,21),thickness=3,lineType=cv2.LINE_AA)

#drawing a arrowed line
cv2.arrowedLine(canvas,(240,230),(300,420),(255,255,0), tipLength=0.3)
cv2.imshow("geometry shapes", canvas)
cv2.waitKey(2000)