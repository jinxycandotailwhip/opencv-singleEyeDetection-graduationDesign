import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)  #高斯随机序列 均值：0 方差：20 输出个数：3个
            b = image[row, col, 0]  #blue
            g = image[row, col, 1]  #green
            r = image[row, col, 2]  #red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise_image", image)



def blur_image(image):
    kernel_self = np.ones([5, 5], np.float32)/25
    dst = cv.filter2D(image, -1, kernel=kernel_self)
    cv.imshow("blur_photo", dst)

def sharpen(image):
    kernel_self = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel_self)
    cv.imshow("blur_photo", dst)

src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/image01.jpg")
#cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
#blur_image(src)
#sharpen(src)
t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()*1000
print("time consume:%s" % time)
dst = cv.GaussianBlur(src, (5, 5), 0)
cv.imshow("gaussian_blur", dst)
cv.waitKey(0)

cv.destroyAllWindows()