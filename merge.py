import cv2
import os
import shutil
# from config import fg_video_path
origin_video_path = r"...\OriginVedio.mp4"


def become_video(output_figure):
    cap = cv2.VideoCapture(origin_video_path)
    fgs = int(cap.get(cv2.CAP_PROP_FPS))
    pictrue_in_filelist = os.listdir(output_figure)
    name = output_figure + "/" + pictrue_in_filelist[0]
    img = cv2.imread(name)
    h, w, c = img.shape
    size = (w, h)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_video = output_figure + '.avi'
    video_writer = cv2.VideoWriter(out_video, fourcc, fgs, size)

    for i in range(len(pictrue_in_filelist)):
        pictrue_in_filename = output_figure + "/" + pictrue_in_filelist[i]
        img12 = cv2.imread(pictrue_in_filename)
        video_writer.write(img12)
    video_writer.release()
    print("删除合成的图片数据集")
    shutil.rmtree(output_figure)
    return out_video


if __name__ == '__main__':
    video = become_video(r"...\output")
