"""
模板匹配
这里和hsv追踪颜色不同，是通过和样本的方差，相关度，卡方的比对来找到模板所对应的位置
三种匹配方法
其中type(cv.TM_SQDIFF_NORMED)是int
假枚举类型
"""
import cv2 as cv


def template_demo():
    tpl = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1_sample2.jpg")
    target = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/brz1.jpg")
    cv.imshow("tpl", tpl)
    cv.imshow("target", target)
    method = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in method:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        cv.imshow("match-" + str(md), target)


template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
