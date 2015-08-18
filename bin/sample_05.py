# coding: UTF-8
import numpy as np
import cv2
import cv2.cv as cv

updatelock = False # トラックバー処理中のロックフラグ
windowname_in = 'inframe' # Window(元画像)の名前
windowname_out = 'outframe' # Window(変換画像)の名前
trackbarname = 'Position' # トラックバーの名前

# AVIファイルを読む
cap = cv2.VideoCapture('out/camera_sample.m4v')

# トラックバーを動かしたときに呼び出されるコールバック関数の定義
def onTrackbarSlide(pos):
    updatelock = True
    cap.set(cv.CV_CAP_PROP_POS_FRAMES, pos)
    updatelock = False

# Cannyエッジ検出
def doCanny(img):
    # カラー画像をグレー画像に変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, 100, 200)

# 名前付きWindowを定義する
cv2.namedWindow(windowname_in, cv2.WINDOW_NORMAL)
cv2.namedWindow(windowname_out, cv2.CV_WINDOW_AUTOSIZE)

# AVIファイルのフレーム数を取得する
frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))

# フレーム数が1以上ならトラックバーにセットする
if (frames > 0):
    cv2.createTrackbar(trackbarname, windowname_in, 0, frames, onTrackbarSlide)

# AVIファイルを開いている間は繰り返し
while(cap.isOpened()):

    # トラックバー更新中は描画しない
    if (updatelock):
        continue

    # １フレーム読む
    ret, frame = cap.read()

    # 読めなかったら抜ける
    if ret == False:
        break

    # 画面に表示
    cv2.imshow(windowname_in,frame)
    cv2.imshow(windowname_out,doCanny(frame))

    # 現在のフレーム番号を取得
    curpos = int(cap.get(cv.CV_CAP_PROP_POS_FRAMES))

    # トラックバーにセットする（コールバック関数が呼ばれる）
    cv2.setTrackbarPos(trackbarname, windowname_in, curpos)

    # qを押したら抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# AVIファイルを解放
cap.release()

# Windowを閉じる
cv2.destroyAllWindows()
