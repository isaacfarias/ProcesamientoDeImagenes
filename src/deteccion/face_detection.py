import os
import cv2


abs_path = os.path.dirname(__file__)
TRAINSET = os.path.join(abs_path,"haarcascades/haarcascade_frontalface_alt.xml")

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier(TRAINSET)
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    cv2.imwrite('img/detected.jpg', img) #cambiar a

rects, img = detect("img/megan.jpg")
box(rects, img)