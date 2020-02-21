import cv2 as cv


def face_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier('D:/studyfuckinghard/graduationcv'
                                         '/opencv-master/opencv-master/data/haarcascades'
                                         '/haarcascade_frontalface_alt_tree.xml')
    faces = face_detector.detectMultiScale(gray, 1.1, 2)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv.imshow("face_detection", image)


#src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/kids.jpg")
capture = cv.VideoCapture(0)
cv.namedWindow("face_detection", cv.WINDOW_AUTOSIZE)
while True:
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    face_detection(frame)
    c = cv.waitKey(10)
    if c == 27:
        break
#face_detection(src)
cv.destroyAllWindows()
