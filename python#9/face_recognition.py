import dlib

import cv2

# read img
imgs = cv2.imread("pa.jpg")

# convert to grayscale
gray = cv2.cvtColor(src=imgs, code=cv2.COLOR_BGR2GRAY)
# dlib: load face recognition Detector
face_recognition = dlib.get_frontal_face_detector()
faces = face_recognition(gray)
for face in  faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    cv2.rectangle(img=imgs, pt1=(x1,y1), pt2=(x2, y2), color=(0,255,0), thickness=3)
  

# show img
cv2.imshow(winname='photo app', mat=imgs)

# wait for a key press to exit
cv2.waitKey(delay=0)

# close all windows
cv2.destroyAllWindows()

