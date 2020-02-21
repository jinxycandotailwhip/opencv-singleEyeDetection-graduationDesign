"""
霍夫变换这里对预处理的要求高
在滤波方面可以选择两种方法
霍夫圆检测对噪声敏感
需要提前边缘保留滤波
opencv中找圆心得方法是梯度方向方法
param1 canny检测的双阈值中的高阈值，低阈值是它的一半
param2 最小投票数（基于圆心的投票数）
minRadius 需要检测院的最小半径
maxRadius 需要检测院的最大半径
返回值是：圆心横纵坐标和半径
"""
import cv2 as cv
import numpy as np


def hough_circle_demo(image):
    #dst = cv.pyrMeanShiftFiltering(image, 10, 90)
    dst = cv.bilateralFilter(image, 0, 100000, 6)
    cv.imshow("afterFliter", dst)
    cimg = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimg, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=20, minRadius=0, maxRadius=0)
    print(circles)
    for i in circles[0]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (2555, 0, 0), 2)
    cv.imshow("houghCircleDetection", image)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/coins.png")
cv.imshow("input", src)
hough_circle_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
