# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys



waittime = 1



if __name__ == '__main__':
    warp_type = cv2.MOTION_HOMOGRAPHY
    warp = np.eye(3,3,dtype=np.float32)
    warpTransform = cv2.warpPerspective

    #input movie
    cap = cv2.VideoCapture(sys.argv[1])
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #first frame
    has_next, init_frame = cap.read()
    #frame = cv2.resize(frame, size)
    #((ECC -> using gray img))
    init_frame = cv2.cvtColor(init_frame, cv2.COLOR_BGR2GRAY)

    #output
    out = cv2.VideoWriter(sys.argv[2] + ".mp4", cv2.VideoWriter_fourcc("m", "p", "4", "v"), fps, size)

    #main
    while True:

        has_next, frame = cap.read()
        if not has_next:
            break
        #frame = cv2.resize(frame, size)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #main transform
        cv2.findTransformECC(gray_frame, init_frame, warp, warp_type)
        out_frame = warpTransform(frame, warp, size)


        #cv2.imshow("", out_frame)
        out.write(out_frame)

        #key = cv2.waitKey(waittime)
        #if key == 27:
        #    break

    cap.release()
    out.release()
    cv2.destroyAllWindows()