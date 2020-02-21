"""
其他形态学操作（具体谁减去谁就不深究了）
顶帽（开操作-原图）
黑帽（闭操作-原图）
形态学梯度（腐蚀-膨胀）
内梯度，外梯度（略）
是形态学用于求边缘的方法
"""
import cv2 as cv
import numpy as np


def top_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    top_hat = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    cimg = np.ones(gray.shape, np.uint8)
    cimg = 50
    dst = cv.add(top_hat, cimg)
    cv.imshow("top_hat_demo", dst)


def black_hat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (10, 10))
    black_hat = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cimg = np.ones(gray.shape, np.uint8)
    cimg = 50
    dst = cv.add(black_hat, cimg)
    cv.imshow("black_hat_demo", dst)


def hat_on_binary(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold value is:%s" % ret)
    cv.circle(binary, (300, 200), 4, 0, -1)  # 在正方形内部点一点（为了给闭操作用）
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    black_hat_binary = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("black_hat_binary", black_hat_binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    top_hat_binary = cv.morphologyEx(binary, cv.MORPH_TOPHAT, kernel)
    cv.imshow("top_hat_binary", top_hat_binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    gradient_binary = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("Gradient_binary", gradient_binary)



src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/pillsetc.png")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
# top_hat_demo(src)
# black_hat_demo(src)
hat_on_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()
