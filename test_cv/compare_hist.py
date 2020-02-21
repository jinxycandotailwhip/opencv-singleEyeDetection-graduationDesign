"""
分别把BGR三层的颜色分成16份，一份内包含的色彩深度区间就是bsize=256/16
即把把原先三通道的三维矩阵转换成4096个直方图
按照RGB的顺序转换成一维的坐标
例如b=15,g=15,r=15就是0
b=20,g=20,r=15就是index=1*16*16+1*16+0=272(1,1,0)
index就是横坐标
(0,0,0)(0,0,1)(0,0,2)...(0,0,15)(0,1,0)(0,1,1)(0,1,2)...
0      1      2   ...   15      16     17     18  ...
"""
import cv2 as cv
import numpy as np


def creat_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist


def compare_hist(image1, image2):
    hist1 = creat_rgb_hist(image1)
    hist2 = creat_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("bha：%s, correl：%s, chisqr：%s"%(match1, match2, match3))


src1 = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1.jpg")
src2 = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz2.jpg")
cv.imshow("img1", src1)
cv.imshow("img2", src2)

compare_hist(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
