"""
直方图均衡不改变图像的像素点的位置以及像素点的灰度等级
改变的仅仅是每一个灰度等级的灰度深度
使得图像黑的更黑白的更白
从而得到增加对比度的效果
如果一副8位深度的图像遍布[0,255]的所有深度
那么对于这幅图像直方图均值对此图像不能做出改变

在连续的图像中，均衡化后灰度的分布应该是服从均匀分布的
在离散的数字图像中，均衡化后的灰度分布还是离散的，并不符合均匀分布
而是和原图像的灰度图像类似

限制对比度自适应直方图均衡化算法（划分区域，限制幅值，双线性差值）
可以提升局部的对比度，还可以抑制AHE算法不能抑制的噪声
然后通过双线性差值消除划分区域的边缘效应
clipLimit是限制幅度的大小（局部对比度过高会放大噪点，所以需要通过限制幅值来限制对比度）
tileGirdSize是划分区域的大小
"""
import cv2 as cv


def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equal_demo", dst)


def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=40, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/rick_and_morty.jpg")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
equalHist_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
