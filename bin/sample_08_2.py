# -*- coding: utf-8 -*-

import cv2
import cv2.cv as cv

##### 動画から顔を検出してみる

# トラックバーを動かしたときに呼び出されるコールバック関数の定義
def onTrackbarSlide(pos):
    updatelock = True
    cap.set(cv.CV_CAP_PROP_POS_FRAMES, pos)
    updatelock = False

## カスケードファイル
cascade_path = "/usr/local/Cellar/opencv/2.4.11_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

updatelock = False # トラックバー処理中のロックフラグ
windowname_in = 'inframe' # Window(元画像)の名前
trackbarname = 'Position' # トラックバーの名前

# 動画パス
video_path = "out/camera_sample.m4v"
out_video_path = "out/face_detect_sample.m4v"
# コーデックの指定
fourcc = cv2.cv.CV_FOURCC('m','p','4','v')
# 動画ファイル読み込み
cap = cv2.VideoCapture(video_path)
out = cv2.VideoWriter("face_output.m4v", fourcc, 30.0, (1280,720))

color = (0, 187, 254) #黄
#カスケード分類器をセットする
cascade = cv2.CascadeClassifier(cascade_path)

# 名前付きWindowを定義する
cv2.namedWindow(windowname_in, cv2.WINDOW_NORMAL)

# AVIファイルのフレーム数を取得する
frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
# フレーム数が1以上ならトラックバーにセットする
if (frames > 0):
    cv2.createTrackbar(trackbarname, windowname_in, 0, frames, onTrackbarSlide)

frame_num = 0
img_cnt = 0
# フレームごとの処理
while(cap.isOpened()):
    # トラックバー更新中は描画しない
    if (updatelock):
        continue
    ## フレーム取得
    ret, frame = cap.read()
    if (ret == False):
        break
    ## グレースケールに変換
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    facerect = cascade.detectMultiScale(
        frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

    # 顔の検出
    #print("frame : %d" % frame_num)
    if len(facerect) > 0:
        #検出した顔を囲む矩形の作成
        for (x,y,w,h) in facerect:
            cv2.rectangle(frame, (x,y),(x+w,y+h), color, thickness=7)
            img_cnt += 1
    #out.write(cv2.resize( frame, (1280, 720)) )

    # 画面に表示
    cv2.imshow(windowname_in,frame)
    # 現在のフレーム番号を取得
    curpos = int(cap.get(cv.CV_CAP_PROP_POS_FRAMES))

    # トラックバーにセットする（コールバック関数が呼ばれる）
    cv2.setTrackbarPos(trackbarname, windowname_in, curpos)

    frame_num += 1

cap.release()
cv2.destroyAllWindows()
out.release()
