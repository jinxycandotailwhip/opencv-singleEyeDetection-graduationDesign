import cv2 as cv
import numpy as np
from aoligei import solve_pnp


def match_sift(find_img, img):
    MIN_MATCH_COUNT = 5
    """转换成灰度图片"""
    gray1 = cv.cvtColor(find_img, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    """创建SIFT对象"""
    sift = cv.xfeatures2d.SIFT_create()
    """创建FLAN匹配器"""
    matcher = cv.FlannBasedMatcher(dict(algorithm=1, trees=5), {})
    """检测关键点并计算键值描述符"""
    kpts1, descs1 = sift.detectAndCompute(gray1, None)
    kpts2, descs2 = sift.detectAndCompute(gray2, None)
    """KnnMatt获得Top2"""
    matches = matcher.knnMatch(descs1, descs2, 2)
    """根据他们的距离排序"""
    matches = sorted(matches, key=lambda x: x[0].distance)
    """比率测试，以获得良好的匹配"""
    good = [m1 for (m1, m2) in matches if m1.distance < 0.7 * m2.distance]
    canvas = img.copy()
    """发现单应矩阵"""
    """当有足够的健壮匹配点对（至少个MIN_MATCH_COUNT）时"""
    if len(good) >= MIN_MATCH_COUNT:
        """从匹配中提取出对应点对"""
        """小对象的查询索引，场景的训练索引"""
        src_pts = np.float32([kpts1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kpts2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        """利用匹配点找到CV2.RANSAC中的单应矩阵"""
        M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
        print("单应性矩阵：\n", M)
        """计算图1的畸变，也就是在图2中的对应的位置"""
        h, w = find_img.shape[:2]
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
        #print(pts)
        dst = cv.perspectiveTransform(pts, M)
        print("经过单应性矩阵变换完的四个点在新图中的坐标：\n", dst)

        """绘制边框"""
        cv.polylines(canvas, [np.int32(dst)], True, (0, 255, 0), 3, cv.LINE_AA)
    else:
        print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
        return img
    return canvas, dst


if __name__ == "__main__":
    img1 = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/find_mat.jpg")
    find_img1 = cv.imread("D:/studyfuckinghard/graduationcv/imgtest/mat.jpg")
    result, dst = match_sift(find_img1, img1)
    coordinate = solve_pnp(dst)
    cv.imshow("find_img1", find_img1)
    cv.imshow("img1", img1)
    cv.imshow("result", result)
    cv.imwrite("D:/studyfuckinghard/graduationcv/imgtest/find_mat_result.jpg", result)
    cv.waitKey()
cv.destroyAllWindows()
