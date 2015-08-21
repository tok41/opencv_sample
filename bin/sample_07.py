# -*- coding: utf-8 -*-

import cv2

##### 動画から顔を検出してみる
##### http://hogehuga.com/post-241/

## カスケードファイル
cascade_path = "/usr/local/Cellar/opencv/2.4.11_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

def detect_face(image):
    # グレースケールに変換
    image_gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)
    image_gray = cv2.equalizeHist(image_gray)
    # 認識器を作成する
    cascade = cv2.CascadeClassifier(cascade_path)
    # 顔認識の実行
    facerect = cascade.detectMultiScale(
        image_gray, scaleFactor=1.1, minNeighbors=3, minSize=(50, 50))
    print "face rectangle"
    return facerect

### main 処理 ###
# 処理する動画ファイルを指定
video_path = "out/camera_sample.m4v"
cap = cv2.VideoCapture(video_path)

# 処理の実行
framenum = 0
faceframenum = 0
color = (255, 255, 255)
while(1):
    framenum += 1
    # 1フレーム取ってくる
    ret, image = cap.read()
    if not ret:
        break
 
    # 10フレーム毎に顔認識処理をする
    if framenum%10 == 0:
        facerect = detect_face(image)
        if len(facerect) == 0: continue
        # 検出領域を描く
        for rect in facerect:
            croped = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
            cv2.imwrite("detected" + str(faceframenum) + ".jpg", croped)
        faceframenum += 1
cap.release()

