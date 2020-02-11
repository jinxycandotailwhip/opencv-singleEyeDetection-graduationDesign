"""
先canny
再find contours
"""
import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    #X_gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    #y_gradient
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    #edge
    edge = cv.Canny(xgrad, ygrad, 50, 150)
    print(edge.shape)
    #cv.imshow("Canny_edge", edge)
    return edge


def contours_test(image):
    blackboard = np.zeros(image.shape[:2])
    edges, contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(blackboard, contours, -1, 255, 2)  #-1是指画出contours里所有边缘
    #print(contours)
    i = 0
    for hierarchy_each in hierarchy[0]:  #用i循环画出contours里面所有边缘
        print(hierarchy_each)
        print(i)
        if hierarchy_each[3] == -1:
            cv.drawContours(blackboard, contours, i, 255, 1)
        else:
            pass
        i = i + 1
    cv.imshow("contours", blackboard)
    cv.imshow("return_edges", edges)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/blobs.png")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
src_procceed = edge_demo(src)
contours_test(src_procceed)
cv.waitKey(0)

cv.destroyAllWindows()
