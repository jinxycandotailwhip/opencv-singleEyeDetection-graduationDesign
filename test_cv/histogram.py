import cv2 as cv
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()


def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):  #枚举的遍历i是对象的编号color是对象的值
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)  #画线红色用红色蓝色用蓝色绿色用绿色
        plt.xlim([0, 256])
    plt.show()




src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/image01.jpg")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
#plot_demo(src)
#image_hist(src)
cv.waitKey(0)

cv.destroyAllWindows()