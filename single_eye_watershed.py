"""
使用分水岭算法得到边缘
在二值图像上显示出来（其实是灰度图像）
就是把分水岭最后一步描边不在原图上描（给了一张黑纸描）
这个文件里不需要边缘太分明，只需要有大致轮廓，只需要前景的整块，不需要分割前景间的边界
增加确定是前景的区域
"""
import cv2 as cv
import numpy as np


def watershed_demo(image):
    binary_show = np.ones(image.shape[:2], dtype=np.uint8)
    blurred = cv.pyrMeanShiftFiltering(image, 10, 50)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    #cv.imshow("pre_operation_binary", binary)

    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=3)
    mb = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel, iterations=3)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    sure_bg = cv.morphologyEx(sure_bg, cv.MORPH_CLOSE, kernel, iterations=3)
    #cv.imshow("sure_bg", sure_bg)

    # distance_transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    #cv.imshow("dist_output", dist_output * 50)

    # 得到sure_fg的二值图像
    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    #cv.imshow("sure_fg", surface)

    sure_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg, sure_fg)  # 未知区域
    ret, markers = cv.connectedComponents(sure_fg)
    cv.imshow("unknown", unknown)
    print("number of components:%s" % ret)

    # watershed_transform
    markers = markers + 1

    markers[unknown == 255] = 0  #把unknown里面等于255的像素点都变成0
    markers = cv.watershed(image, markers=markers)
    binary_show[markers == -1] = 255  #把markers=-1的点都标红（画出分水岭）
    cv.imshow("watershed_src", binary_show)


while True:
    capture = cv.VideoCapture(0)
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    watershed_demo(frame)
    c = cv.waitKey(30) & 0xff
    if c == 27:
        break
cv.waitKey(0)
cv.destroyAllWindows()
