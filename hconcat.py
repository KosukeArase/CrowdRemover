# -*- coding: utf-8 -*-

import cv2
import sys
import util
import time
import numpy as np


class Config(object):
    ESC_KEY = 27     # Escキー
    INTERVAL= 33     # インターバル

    WINDOW_ORG = "original"
    WINDOW_BACK = "back"
    WINDOW_DIFF = "diff"

    # min_size = 50 # for youtube_1_1.mp4
    min_size = 400 # for other movies
    lr = 0.01 # Learing Rate. The smaller lr is, the more sensitive the system is.


def get_config():
    return Config()


def set_windows():
    cv2.namedWindow(config.WINDOW_ORG)
    cv2.namedWindow(config.WINDOW_BACK)
    cv2.namedWindow(config.WINDOW_DIFF)


def video_output(x, y):
    _fps = 30
    _capSize = (x, y) # this is the size of my source video
    _fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    # _fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    _out = cv2.VideoWriter()
    # _flag = _out.open(FILE_DST+".mp4", _fourcc, _fps, _capSize, True)
    # _flag = _out.open(FILE_ORG.split(".")[0]+"_teiten.mp4", _fourcc, _fps, _capSize, True)
    _flag = _out.open(FILE_DST+".mp4", _fourcc, _fps, _capSize, True)

    return _flag, _out


def process():
    # if algorithm == "accumulateWeighted":
    #     _f_frame = _i_frame.astype(np.float32) # convert pixel to float
    #     _diff_frame = cv2.absdiff(_f_frame, back_frame) # calc diff between frame and background
    #     cv2.accumulateWeighted(_f_frame, back_frame, 0.025) # update background
    #     _img_binary, _img_back = util.modify_image(_diff_frame.astype(np.uint8)) # binarize
    #     cv2.imshow("diff", _diff_frame.astype(np.uint8))
    #     cv2.imshow("back", back_frame.astype(np.uint8))
    # elif algorithm == "backgroundSubtractor":
    #     _img_binary = fgbg.apply(_i_frame, learningRate = config.lr)
    #     # print dir(fgbg)
    #     _img_binary = cv2.morphologyEx(_img_binary, cv2.MORPH_OPEN, kernel)
    #     _img_binary = cv2.morphologyEx(_img_binary, cv2.MORPH_CLOSE, kernel)
    #     _img_back = fgbg.getBackgroundImage()
    # else:
    #     print "wrong algorithm in process()"

    # util.draw_approx_rect(_i_frame, _img_back, config.min_size) # detect object
    # cv2.imshow(config.WINDOW_ORG, _i_frame)
    # cv2.imshow(config.WINDOW_BACK, _img_back)
    # print(dir(_i_frame), dir(_img_back))
    # diff = np.sum(_i_frame - _img_back)
    # print(diff)

    concat = cv2.hconcat([i_frame2, i_frame1])
    # cv2.imshow('unko', concat)
    # _key = cv2.waitKey(config.INTERVAL)

    out.write(concat.astype(np.uint8)) # write frame
    # out.write(_img_back) # write frame
    _has_next1, _i_frame1 = mov_org1.read() # next frame
    _i_frame1 = cv2.resize(_i_frame1, (480, 720))
    _has_next2, _i_frame2 = mov_org2.read() # next frame

    return _has_next1, _i_frame1, _has_next2, _i_frame2


if __name__ == "__main__":
    config = get_config()
    set_windows()

    # FILE_ORG = "movies/takakura_trimmed.mov"
    FILE_ORG1 = sys.argv[1]
    FILE_ORG2 = sys.argv[2]
    FILE_DST = sys.argv[3]

    # mov_org = cv2.VideoCapture(0)
    mov_org1 = cv2.VideoCapture(FILE_ORG1)
    mov_org2 = cv2.VideoCapture(FILE_ORG2)

    has_next1, i_frame1 = mov_org1.read() # first frame
    i_frame1 = cv2.resize(i_frame1, (480, 720))

    has_next2, i_frame2 = mov_org2.read() # first frame
    print(i_frame1.shape, i_frame2.shape)

    success, out = video_output(len(i_frame2[0])*2, len(i_frame2))
    if not success:
        print "error in opening VideoWriter()"

    # background frame for AccumulateWeighted algorithm (choose the way to calculate background)
    # back_frame = np.zeros_like(i_frame, np.float32) # 逐次的に計算(背景差分法)
    # back_frame = cv2.imread(FILE_ORG.split(".")[0]+".jpg", 1).astype(np.float32) # (前もって画素値の平均を算出)

    # background subtraction object
    # fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = False)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

    t = time.time()

    # frame = 0
    while has_next1 and has_next2:

        """ choose the algorithm """
        # has_next, i_frame = process(i_frame, "accumulateWeighted")
        has_next1, i_frame1, has_next2, i_frame2 = process()
        # has_next, i_frame = process(i_frame, "backgroundSubtractor")
        # frame += 1
        # if frame == 16*30:


    tt = time.time()

    print tt - t

    out.release()
    mov_org1.release()
    mov_org2.release()
    cv2.destroyAllWindows()


