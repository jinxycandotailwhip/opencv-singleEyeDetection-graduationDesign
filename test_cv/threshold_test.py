"""
局部二值化cv.adaptiveThreshold中
cv.ADAPTIVE_THRESH_MEAN_C是方法
25分割的大小，一定要是奇数
10是一个阈值可以允许的波动范围（防止噪声）
图像亮度有差异的情况下尽量选择局部自适应阈值化
"""
import cv2 as cv


def threshold_demo(image):  #全局阈值
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value is:%s" % ret)
    cv.imshow("binary1", binary)


def local_threshold_demo(image):  #自适应阈值（分块）
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow("binary2", dst)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1.jpg")
threshold_demo(src)
local_threshold_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
