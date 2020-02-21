import cv2 as cv
import numpy as np

def lapalian(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian", lpls)


def sobel_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    #cv.imshow("gradient_x", gradx)
    #cv.imshow("gradient_y", grady)
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient_xy", gradxy)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1.jpg")
sobel_demo(src)
lapalian(src)
cv.waitKey(0)
cv.destroyAllWindows()