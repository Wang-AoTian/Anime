
import cv2
import logging

# log information settings
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def save_image(num, image):
    """Save the images.

    Args:
        num: serial number
        image: image resource

    Returns:
        None
    """

    image_path = "D:\Code\Python\Cartnoon\src\{}.png".format(str(num))
    cv2.imwrite(image_path, image)


file_path = "D:\Code\Python\Cartnoon\OriginVedio.mp4"

vc = cv2.VideoCapture(file_path)  # import video files

# determine whether to open normally
if vc.isOpened():
    ret, frame = vc.read()
else:
    ret = False

count = 0  # count the number of pictures
frame_interval = 2  # video frame count interval frequency
frame_interval_count = 0

# loop read video frame
while ret:
    ret, frame = vc.read()
    # store operation every time f frame
    if frame_interval_count % frame_interval == 0:
        save_image(count, frame)
        logging.info("num：" + str(count) + ", frame: " +
                     str(frame_interval_count))
        count += 1
    frame_interval_count += 1
    cv2.waitKey(1)

vc.release()
