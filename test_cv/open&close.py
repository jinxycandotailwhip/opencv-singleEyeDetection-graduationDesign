"""
开操作可以去除外部小的噪点
闭操作可以填充图形内部的小点
API使用层面要注意结构元素的大小和结构元素的形状
用(15,1)横着的开操作可以提取横线
用(1,15)竖着的开操作可以提取竖线
"""
import cv2 as cv


def open_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
    binary_open = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
    cv.imshow("open_demo", binary_open)


def close_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (10, 10))
    binary_close = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
    cv.imshow("close_demo", binary_close)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/pillsetc.png")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
print("threshold value is:%s" % ret)
cv.circle(binary, (300, 200), 4, 0, -1)  #在正方形内部点一点（为了给闭操作用）
cv.imshow("binary", binary)
src = binary.copy()  #这之前都在画符合要求的图片
open_demo(src)
close_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
