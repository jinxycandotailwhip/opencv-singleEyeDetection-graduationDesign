import cv2 as cv
import time
from aoligei_sift import match_sift
from aoligei import solve_pnp
from moviepy.editor import ImageSequenceClip


def read_video(video_path, image):
    found_list = []
    # 打开视频文件：在实例化的同时进行初始化
    cap = cv.VideoCapture(video_path)
    # 检测是否正常打开：成功打开时，isOpened返回ture
    while cap.isOpened():
        # 获取每一帧的图像frame
        ret, frame = cap.read()
        # 这里必须加上判断视频是否读取结束的判断,否则播放到最后一帧的时候出现问题了
        if ret:
            start = time.time()
            # 将从视频中的获取的图像与要找的图像进行匹配
            found, dst = match_sift(image, frame)
            coordinate = solve_pnp(dst)
            text = "coordinate" + str(coordinate)
            cv.putText(found, text, (100, 100), cv.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 2)
            end = time.time()
            print(end-start)
            # 获取原图像的大小
            width, height = found.shape[:2]
            # 将原图像缩小到原来的二分之一
            #size = (int(height/2), int(width/2))
            #found = cv.resize(found, size, interpolation=cv.INTER_AREA)
            # 显示图片
            found_RGB = cv.cvtColor(found, cv.COLOR_BGR2RGB)
            found_list.append(found_RGB)
            cv.imshow("found", found)
            cv.waitKey(30)
        else:
            break
        # 因为视频是7.54帧每秒，因此每一帧等待133ms - 62ms
        #if cv.waitKey(133-int((end-start)*1000)) & 0xFF == 27:
            #break
    return found_list
    # 停止在最后的一帧图像上
    cv.waitKey()
    # 如果任务完成了，就释放一切
    cap.release()
    # 关掉所有已打开的GUI窗口
    cv.destroyAllWindows()


if __name__ == "__main__":
    # 视频的路径
    video_path = 'D:/studyfuckinghard/graduationcv/imgtest/find_mat5.mp4'
    # 要匹配图片的路径
    image_path = 'D:/studyfuckinghard/graduationcv/imgtest/mat.jpg'
    # 读取一张图片
    image = cv.imread(image_path)
    # 读取视频，并识别
    found_list = read_video(video_path, image)
    clip = ImageSequenceClip(found_list, fps=25)
    clip.write_videofile("D:/studyfuckinghard/graduationcv/imgtest/find_mat_done_aoligei.mp4", codec='mpeg4',
                         verbose=False,
                         audio=False)
