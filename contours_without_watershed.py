"""
使用目标追踪获取ROI区域
findcontours直接获取轮廓并得到轮廓的面积信息
"""
import cv2 as cv
import numpy as np


def watershed_demo(image):
    print("image shape:" + str(image.shape))
    blurred = cv.pyrMeanShiftFiltering(image, 10, 50)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    # morphology operation
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=3)
    mb = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel, iterations=4)

    return mb


def measure_contours(image):
    blackboard = np.zeros(image.shape[:2], np.uint8)
    ret_image, contours, hierarchy = cv.findContours(image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print(hierarchy)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        mm = cv.moments(contour)  #contour的几何矩
        if bool(mm["m00"]):
            cx = mm["m10"]/mm["m00"]
            cy = mm["m01"]/mm["m00"]
            cv.circle(image, (int(cx), int(cy)), 3, 255, -1)
        else:
            pass
        cv.drawContours(blackboard, contours, i, 255, 2)
        cv.imshow("contours", ret_image)
        cv.putText(blackboard, "area:%s" % area, (100, 20), cv.FONT_HERSHEY_SIMPLEX, 0.75, 255, 1)
        return blackboard


tracker = cv.TrackerMedianFlow_create()
video = cv.VideoCapture(0)
ret, frame = video.read()
bbox = cv.selectROI("ROI_select_window", frame, False)
tracker.init(frame, bbox)

while True:
    ret, frame = video.read()
    if not ret:
        break
    roi_in_whole = np.zeros(frame.shape[:2], np.uint8)
    ret, bbox = tracker.update(frame)
    if ret:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv.putText(frame, "Tracking failure detected", (100, 80), cv.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)
    cv.imshow("Tracking", frame)

    #使用追踪出来的ROI区域使用分水岭算法
    ROI = frame[int(bbox[1]):int(bbox[1]+bbox[3]), int(bbox[0]):int(bbox[0]+bbox[2])]
    cv.imshow("ROI", ROI)
    blackboard = watershed_demo(ROI)
    roi_in_whole[int(bbox[1]):int(bbox[1]+bbox[3]), int(bbox[0]):int(bbox[0]+bbox[2])] = blackboard
    sized_pic = measure_contours(roi_in_whole)
    cv.imshow("sized_pic", sized_pic)
    k = cv.waitKey(1) & 0xff
    if k == 27:
        break
