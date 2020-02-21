"""
也可以对彩色图像进行操作
膨胀是用最大值取代中心像素（亮的的地方周围更亮）
腐蚀是用最小值取代中心像素（暗的地方周围更暗）
"""
import cv2 as cv
import numpy as np


def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)


def dilation_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilation_demo", dst)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/pillsetc.png")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
#erode_demo(src)
dilation_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
