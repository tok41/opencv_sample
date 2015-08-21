# -*- coding: utf-8 -*-

import cv2

##### 動画から顔を検出してみる

## カスケードファイル
cascade_path = "/usr/local/Cellar/opencv/2.4.11_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

# 動画パス
video_path = "out/camera_sample.m4v"
out_video_path = "out/face_detect_sample.m4v"

color = (0, 187, 254) #黄
#カスケード分類器をセットする
cascade = cv2.CascadeClassifier(cascade_path)

# コーデックの指定
fourcc = cv2.cv.CV_FOURCC('m','p','4','v')
# 動画ファイル読み込み
cap = cv2.VideoCapture(video_path)
out = cv2.VideoWriter("face_output.m4v", fourcc, 30.0, (1280,720))

frame_num = 0
img_cnt = 0
# フレームごとの処理
while(cap.isOpened()):
    ## フレーム取得
    ret, frame = cap.read()
    if (ret == False):
        break
    ## グレースケールに変換
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(
        frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

    print("frame : %d" % frame_num)
    if len(facerect) > 0:
        #検出した顔を囲む矩形の作成
        for (x,y,w,h) in facerect:
            cv2.rectangle(frame, (x,y),(x+w,y+h), color, thickness=7)
            img_cnt += 1
    #out.write(frame)
    out.write(cv2.resize( frame, (1280, 720)) )
    frame_num += 1

cap.release()
cv2.destroyAllWindows()
out.release()
