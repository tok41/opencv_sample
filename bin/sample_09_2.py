# -*- coding: utf-8 -*-

import cv2
import cv2.cv as cv
import numpy as np

##### 動画から顔を検出してみる
##### Webカメラの画像をリアルタイムで処理させる

## カスケードファイル
cascade_path = "/usr/local/Cellar/opencv/2.4.11_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

## 貼り付け画像の読み込み
### ネコ
cat1 = cv2.imread('data/img_neko_01.jpg', 1)
cat2 = cv2.imread('data/img_neko_02.jpg', 1)
### 広告
img_ad = cv2.imread('data/img_ad_01.jpg', 1)

## 顔検出ラインの色指定
color_line = (255, 0, 50)

## カメラのオープン
cap = cv2.VideoCapture(0)
## カスケードファイルのセット
cascade = cv2.CascadeClassifier(cascade_path)

img_flg = 0
while(True):
    ## カメラの画像をキャプチャする
    ret, frame = cap.read()
    if (ret == False):
        print('error : reading image at WebCamera')
        break

    ## 処理を軽くするためにグレースケールに変換
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ## 処理を軽くするために、画像を小さくする(1/4する)
    frame_gray = cv2.resize(frame_gray, (frame.shape[1]/4, frame.shape[0]/4))
    ## 顔部分の探索
    facerect = cascade.detectMultiScale(
        frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
    ## 表示画像の作成
    img_cnt = 0
    if len(facerect) > 0:
        #検出した顔を囲む矩形の作成
        for (x,y,w,h) in facerect:
            ## 1/4したので、４倍する
            x *= 4
            y *= 4
            w *= 4
            h *= 4
            if img_flg == 0:
                ## 矩形領域を書き込む
                cv2.rectangle(frame, (x,y),(x+w,y+h), color_line, thickness=7)
            elif img_flg == 1:
                ## 画像を貼り付ける
                paste_img = cv2.resize(cat1, (h, w))
                frame[y:y+h, x:x+w] = paste_img
            elif img_flg == 2:
                paste_img = cv2.resize(cat2, (h, w))
                frame[y:y+h, x:x+w] = paste_img
            elif img_flg == 3:
                paste_img = cv2.resize(img_ad, (h, w))
                frame[y:y+h, x:x+w] = paste_img
            else :
                frame = frame
            img_cnt += 1
    ## 画面に表示
    cv2.imshow('detect_faces',frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break
    elif k == ord('0'):
        img_flg = 0
    elif k == ord('1'):
        img_flg = 1
    elif k == ord('2'):
        img_flg = 2
    elif k == ord('3'):
        img_flg = 3
    ### 'q'が押されたら終了
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

## 終了処理
cap.release()
cv2.destroyAllWindows()
