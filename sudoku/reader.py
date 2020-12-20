# import cv2  # this works but doesn't resolve names in PyCharm
import cv2.cv2 as cv


def read_img(img_src: str):
    return cv.imread(img_src, cv.IMREAD_GRAYSCALE)
