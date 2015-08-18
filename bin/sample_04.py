# coding: UTF-8
import numpy as np
import cv2

# カメラからのキャプチャ指定
cap = cv2.VideoCapture(0)

# コーデックの指定
fourcc = cv2.cv.CV_FOURCC('m','p','4','v')

# 保存ファイルとフレームレートとサイズの指定
out = cv2.VideoWriter('out/camera_sample.m4v',fourcc, 30, (640,480))

# カメラオープン中はずっと処理する
while(cap.isOpened()):

    # キャプチャ画像を取り出す
    ret, frame = cap.read()

    # データがなければ抜ける
    if ret==False:
        break

    # 画像をファイルに書き込む
    out.write(cv2.resize( frame, (640, 480)) )

    # 画像を画面に出力する
    cv2.imshow('frame',frame)

    # "q"が押されたら抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 後始末
cap.release()
out.release()
cv2.destroyAllWindows()
