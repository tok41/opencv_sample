# -*- coding: utf-8 -*-

import cv2

##### 画像から顔を検出してみる

## カスケードファイル
cascade_path = "/usr/local/Cellar/opencv/2.4.11_2/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"
## 読み込むデータ
#image_path = "data/Lenna.png"
image_path = "data/face_3.jpeg"

# これは、BGRの順になっている気がする
color = (255, 255, 255) #白

# 画像の読み込み
image = cv2.imread(image_path)
# グレースケール変換
gray = cv2.cvtColor(image, cv2.cv.CV_BGR2GRAY)

# 分類器を作る?みたいな作業
cascade = cv2.CascadeClassifier(cascade_path)

# 顔認識の実行
facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

if len(facerect) > 0:
    # 検出した顔を囲む矩形の作成
    for rect in facerect:
        cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
else:
    print("no face")

# 認識結果の表示
cv2.imshow("detected.jpg", image)

# 何かキーが押されたら終了
while(1):
    if cv2.waitKey(10) > 0:
        break

