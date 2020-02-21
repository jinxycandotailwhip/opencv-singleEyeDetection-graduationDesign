"""
超大图像二值化
要自己先把图像分割
再进行阈值化
这里的主要内容是分割图像
这里的分割还是有点问题。。。搞不懂
row是纵坐标     ch
col是横坐标     cw
"""
import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)
    h, w = image.shape[:2]
    ch = 256
    cw = 256
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("original", gray)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+cw, col:ch+col]  #划分roi区域
            cv.imshow("roi", roi)  #显示roi区域
            cv.waitKey()
            print("tl:(%s,%s)  roi_size=%s" % (col, row, roi.shape))
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 15)
            gray[row:row+cw, col:col+ch] = dst
            print(np.std(dst), np.mean(dst))
    cv.imshow("binary", gray)
    cv.imwrite("D:/studyfuckinghard/graduationcv/imgtest/binary_test.png", gray)  #保存图片


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1.jpg")
big_image_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()
