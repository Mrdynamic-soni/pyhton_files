import cv2

capture = cv2.VideoCapture(r'D:\projects\opencv_projects\pyhton_files\rev.mp4')

frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"No. of frames are {frames}")

fps = capture.get(cv2.CAP_PROP_FPS)

height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('D:\projects\opencv_projects\pyhton_files\Rev2.avi',fourcc,fps,(int(width*0.5),int(height*0.5)))

print(f"No. of frames are {frames}")
print(f"FPS is {fps}")
frame_index = frames-1

if(capture.isOpened()):
    while(frame_index!=0):
        capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = capture.read()
        frame = cv2.resize(frame, (int(width*0.5),int(height*0.5)))

        output.write(frame)

        frame_index = frame_index-1

        if(frame_index%100 == 0):
            print(frame_index)

output.release()
capture.release()
cv2.destroyAllWindows()

