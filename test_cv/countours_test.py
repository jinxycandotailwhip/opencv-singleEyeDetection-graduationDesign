"""
查找边缘
在查找边缘的时候可以选择是EXTERNAL（外边缘）还是tree（所有的边缘）
画边缘
"""
import cv2 as cv
import numpy as np


def edge_demo(image):
    #mask1 = np.zeros((900, 1440), dtype=np.uint8)
    #mask1[:450, : 720] = 255
    #cv.imshow("mask1", mask1)
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
    return dst


def contours_test(image):
    dst = cv.GaussianBlur(image, (5, 5), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)

    a, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(image, contours, -1, (0, 0, 255), 2)  #-1是指画出contours里所有边缘
    for i, contour in enumerate(contours):  #用i循环画出contours里面所有边缘
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        print(i)
    cv.imshow("contours", image)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1.jpg")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
#src_procceed = edge_demo(src)
contours_test(src)
cv.waitKey(0)

cv.destroyAllWindows()
