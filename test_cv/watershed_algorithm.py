"""
分水岭算法
灰度为0（黑色）的就是最低点，灰度为255（白色）的为最高点

距离变换，就是把像素点的值换成其和最近的背景像素的距离
cv.connectedComponents(...)返回值是marker的数量和和图片同大小的带标签的图片（0是背景）
所以markers要+1，因为在分水岭注水操作中0是代表未知区域
markers[unknown==255]=0  unknown是和makers同样等大小的图像
这个操作就是把unknown内等于255的像素点在markers的对应像素点置0

分水岭的操作顺序：
1.二值化
2.形态学操作图像
3.找确定的前景和背景区域
4.加水寻找边缘
5.运行分水岭算法之后标签会被改变，-1的标签对应山脊，即边缘，描出边缘
"""
import cv2 as cv
import numpy as np


def watershed_demo(image):
    print("image shape:" + str(image.shape))
    blurred = cv.pyrMeanShiftFiltering(image, 10, 50)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)

    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=3)
    mb = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel, iterations=4)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("mor-opt", sure_bg)

    # distance_transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("dist_output", dist_output * 50)

    # 得到markers的二值图像
    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    cv.imshow("markers", surface)

    sure_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg, sure_fg)  # 未知区域
    ret, markers = cv.connectedComponents(sure_fg)
    cv.imshow("unknown", unknown)
    print("number of components:%s" % ret)

    # watershed_transform
    markers = markers + 1

    markers[unknown == 255] = 0  #把unknown里面等于255的像素点都变成0
    markers = cv.watershed(image, markers=markers)
    image[markers == -1] = [0, 0, 255]  #把markers=-1的点都标红（画出分水岭）
    cv.imshow("watershed_src", image)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/coins.png")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
watershed_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
