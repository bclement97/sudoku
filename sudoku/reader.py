import cv2 as cv

img = None


def read_img(img_src: str):
    global img
    img = cv.imread(img_src, cv.IMREAD_GRAYSCALE)
