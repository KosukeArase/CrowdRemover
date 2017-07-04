# -*- coding: utf-8 -*-

import copy
import cv2
import sys
import numpy as np


def draw_contour(img_src, img_bin):
    im, contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img_src, contours, -1, (0, 255, 0), 3)


def modify_image(img_src):
    # img_src = cv2.imread(path, 1)

    img_back = copy.deepcopy(img_src)
    img_back[:,:,:] = 0
    # img_back = np.zeros_like(img_src, np.int)
    # img_back = np.zeros([len(img_src), len(img_src[0])])

    # img_src[:,:,0] = 0
    # img_src[:,:,1] = 0
    # cv2.imshow("a",img_src)
    # cv2.waitKey()

    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

    img_blur = cv2.GaussianBlur(img_gray, (11, 11), 0)
    max_pixel = 255

    img_binary = cv2.adaptiveThreshold(img_blur, max_pixel, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 3)
    # img_binary = cv2.adaptiveThreshold(img_blur, max_pixel, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)

    return img_binary, img_back

def draw_approx_rect(img_dst, img_bin, min_size):
    contoured, contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    lines = []

    for c in contours:
        if cv2.contourArea(c) < min_size:
            continue
        # print cv2.contourArea(c),

        ### rotated rect ###
        # rect = cv2.minAreaRect(c)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # cv2.drawContours(img_dst, [box], 0, (255, 0, 0), 4)


        ### horizontal rect ###
        x, y, w, h = cv2.boundingRect(c)
        print x, y, w, h
        cv2.rectangle(img_dst, (x, y), (x+w, y+h), (255, 0, 0), 4)

        cv2.drawContours(img_dst, c, -1, (0, 0, 255), 4)
        # cv2.drawContours(img_dst, [approximated_line], -1, (0, 255, 0), 4)

    print ""
    return img_dst, lines