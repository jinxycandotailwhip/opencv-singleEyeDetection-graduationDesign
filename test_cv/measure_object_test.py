"""
这里如果提取到的对象轮廓不理想就黑白颠倒一下
很小的边缘对象会使得mm00=0所以要进行滤波或者判断
这个文件内在findcontours找到边缘的基础上
利用中心矩（这里都是用二值图像计算的）计算了图像的重心位置（可以得到目标的信息主要集中在哪边）
利用外接矩形框起对象
不仅可以使用外接矩形包围对象，还可以使用多边形包围对象
approx_curve = cv.approxPolyDP(contour, 4, True)
第一个参数是countours其中一条轮廓
第二个参数越小拟合得越精确（可能参数大的时候正方形可以拟合圆，参数大的时候就可以用多边形拟合圆）
第三个参数表示边缘是否闭合
获得的返回值approx_curve的shape[0]是拟合的多边形的边数
所以可以用来区分三角形矩形等多边形
"""
import cv2 as cv


def measure_contours(image):
    image_approx = image.copy()
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshold is:%s" % ret)
    cv.imshow("binary image", binary)
    image, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        mm = cv.moments(contour)  #contour的几何矩
        if bool(mm["m00"]):
            cx = mm["m10"]/mm["m00"]
            cy = mm["m01"]/mm["m00"]
            cv.circle(image, (int(cx), int(cy)), 3, (255, 0, 0), -1)
            cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        else:
            pass
        print("contour_area:%s" % area)
        approx_curve = cv.approxPolyDP(contour, 4, True)
        print(approx_curve.shape)
        if approx_curve.shape[0] > 5:
            cv.drawContours(image_approx, contours, i, (0, 0, 255), 2)
        elif approx_curve.shape[0] == 4:
            cv.drawContours(image_approx, contours, i, (255, 0, 0), 2)
        else:
            pass
    cv.imshow("measure_contours", image)
    cv.imshow("detect_shape", image_approx)




src = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/pillsetc.png")
cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
cv.imshow("input_image", src)
measure_contours(src)
cv.waitKey(0)

cv.destroyAllWindows()