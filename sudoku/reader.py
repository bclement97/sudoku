import cv2 as cv


def read_img(img_src: str):
    return cv.imread(img_src, cv.IMREAD_GRAYSCALE)
