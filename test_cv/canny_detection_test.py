"""
其中mask的掩膜操作需要np.uint8八位无符号整型
掩膜操作只分是不是0
1和255对掩膜操作没有区别
要形成彩色的canny
就只是通过掩膜把原图的颜色保存下来了
"""
import cv2 as cv
import numpy as np


def edge_demo(image):
    # mask1 = np.zeros((900, 1440), dtype=np.uint8)
    # mask1[:450, : 720] = 255
    # cv.imshow("mask1", mask1)
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    #X_gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    #y_gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    #edge
    edge = cv.Canny(xgrad, ygrad, 50, 150)
    print(edge.shape)
    cv.imshow("Canny_edge", edge)
    dst = cv.bitwise_and(image, image, mask=edge)  #这个函数的意义在于mask操作而不是与操作，得到的dst是在原图基础上mask边缘
    cv.imshow("Canny_edge_colored", dst)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1.jpg")
cv.imshow("input", src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()