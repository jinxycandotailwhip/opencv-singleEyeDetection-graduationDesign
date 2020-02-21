"""
边缘保留模糊
高斯双边滤波
高斯，加梯度
相当于用梯度截取了一半的高斯核来卷积
"""
import cv2 as cv


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 10)
    cv.imshow("bi_demo", dst)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/image01.jpg")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
bi_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
