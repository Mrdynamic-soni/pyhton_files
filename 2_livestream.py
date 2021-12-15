import cv2
capture = cv2.VideoCapture(0)
fourcc =  cv2.VideoWriter_fourcc(*"XVID")
capture_save = cv2.VideoWriter("2_livestream_cap.mp4",fourcc,36.0,(640,480))
while capture.isOpened():
    ret, frame = capture.read()
    if ret == True:
        capture_save.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # to show video in graysacle
        # By default video is in bgr
        cv2.imshow("frames", frame) 
 
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
       # if cv2.waitKey() == ord("s"):
       #     cv2.imwrite("2_livestream_cap.mp4",)

capture.release()
capture_save.release()
cv2.destroyAllWindows()