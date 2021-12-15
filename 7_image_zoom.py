import cv2
import numpy as np

image = cv2.imread("D:\\projects\\opencv_projects\\pyhton_files\\imresize.jpg")

try:
    image_sized = cv2.resize(image,(300,300))
    image_resize = cv2.resize(image,None, fx=1.5,fy=1.5, interpolation=cv2.INTER_LINEAR)
    cv2.imshow("rezised",image_resize)
except Exception as e:
    print(e)





if (cv2.waitKey() == ord('q')):
    cv2.destroyAllWindows()