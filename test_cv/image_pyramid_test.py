"""
图像金字塔
高斯金字塔和拉普拉斯金字塔
pyrDown降采样（先高斯模糊再隔行（列）删除）
pyrUp向上expand（先用全0隔行（列）填充图像，再高斯模糊）
拉普拉斯金字塔就是用高斯金字塔的一层减去下面一层expand的结果
得到的是向上expand所丢失的边缘信息（不是全部边缘信息）
!!!!!要注意的是拉普帕斯金字塔输入的图片一定要长款是2的倍数
"""
import cv2 as cv


def reshape_image(image):
    new_image = image[-512:, -512:]
    cv.imshow("new_image", new_image)
    return new_image


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_image = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_image.append(dst)
        cv.imshow("pyramid"+str(i+1), dst)
        temp = dst.copy()
    return pyramid_image


def laplaian(image):
    pyramid_image = pyramid_demo(image)
    level = len(pyramid_image)
    for i in range(level-1, -1, -1):  #从2到0，步长是-1
        if (i-1) < 0:
            expand = cv.pyrUp(pyramid_image[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("laplaian_down_"+str(i+1), lpls)
        else:
            expand = cv.pyrUp(pyramid_image[i], dstsize=pyramid_image[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_image[i - 1], expand)
            cv.imshow("laplaian_down_" + str(i + 1), lpls)


src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1.jpg")
#cv.imshow("input_image", src)
raw_image = reshape_image(src)
pyramid_demo(raw_image)
laplaian(raw_image)
cv.waitKey(0)
cv.destroyAllWindows()