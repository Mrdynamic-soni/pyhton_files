import cv2
img = cv2.imread("sumu.jpg",1)
print(img)
cv2.imshow("image", img)
cv2.waitKey(1000)


cv2.imwrite("sumu.png", img)