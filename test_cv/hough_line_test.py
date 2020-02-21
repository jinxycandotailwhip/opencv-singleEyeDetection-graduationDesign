"""
第一个函数可以返回线段，还可以限制minlinelengh和maxlinegap
第二个函数只能返回直线
"""
import cv2 as cv
import numpy as np


def hough_possible_line(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray, 50, 150)
    lines = cv.HoughLinesP(edge, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("hough_possible_line", image)


def hough_line(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray, 50, 150)
    lines = cv.HoughLines(edge, 1, np.pi/180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*a)
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*a)
        print("lines(%s,%s),(%s,%s)" % (x1, y1, x2, y2))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("houghLines", image)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/linetest2.jpg")
cv.imshow("input", src)
hough_line(src)
hough_possible_line(src)
cv.waitKey(0)
cv.destroyAllWindows()
