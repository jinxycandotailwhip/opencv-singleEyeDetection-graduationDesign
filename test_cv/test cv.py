import cv2 as cv
import numpy as np


def blur_image(image):
    dst = cv.blur(image, (5, 5))
    cv.imshow("blur_photo", dst)


def capture_blue():
    capture = cv.VideoCapture(0)
    while 1:
        ret, frame = capture.read()
        if ret == False:
            break
        else:
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            lower_hsv = np.array([100, 43, 46])
            upper_hsv = np.array([124, 255, 255])
            mask = cv.inRange(hsv, lower_hsv, upper_hsv)
            dst = cv.bitwise_and(frame, frame, mask=mask)
            cv.imshow("original_video", frame)
            cv.imshow("mask", dst)
            c = cv.waitKey(40)
            if c == 27:
                break


def create_image():
    image = np.zeros([400, 400, 3], np.uint8)
    cv.imshow("image", image)
    image[:, :, 0] = np.ones([400, 400]) * 255
    cv.imshow("ChangedImage", image)


def video_demo():
    # 0是代表摄像头编号，只有一个的话默认为0
    capture = cv.VideoCapture(0)
    while 1:
        ref, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("LocalCamera", frame)
        # 等待30ms显示图像，若过程中按“Esc”退出
        c = cv.waitKey(30) & 0xff
        if c == 27:
            capture.release()
            break


# video_demo()
#create_image()
#capture_blue()
src = cv.imread("D/studyfuckinghard/graduationcv/imgtest/brz.jpg")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("original_photo", src)
blur_image(src)
cv.waitKey(0)

cv.destroyAllWindows()
