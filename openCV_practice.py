#!/usr/bin/env python

from copy import deepcopy
import numpy
import cv2
from matplotlib import pyplot


def read_image(image, color_space=1):
    return cv2.imread(image, color_space)


def show_image(image, name_of_window='image'):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


bw_img = read_image('pexels-angelo-herreras-16881617.jpg', 0)
color_img = read_image('pexels-angelo-herreras-16881617.jpg')
img_to_analyse = deepcopy(color_img)
circle = cv2.circle(img_to_analyse, (2664, 1995), 400, (125, 50, 39), 20)
# show_image(bw_img, 'bw_img')
# show_image(color_img, 'color_img')
show_image(circle, 'circle')
