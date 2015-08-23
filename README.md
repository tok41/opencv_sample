# PythonでOpenCVを使ったプログラムを書いてみるテスト

## サンプルコード(bin以下)

### sample_01.py

* 引数に画像ファイルを指定し、その画像を単純に表示するだけ。
* ↓を参考に
  http://www.takunoko.com/blog/pyenv%E3%81%A7python%E3%81%AEopencv%E7%92%B0%E5%A2%83%E3%82%92%E6%95%B4%E3%81%88%E3%82%8B/

```
 $ python bin/sample_01.py {画像ファイル}
```

### sample_02.py

* 動画ファイル（AVI motion jpeg）を再生するだけ。
  * 動画ファイルはハードコーディングされている
  * 引数なし
* ↓を参考に
  http://qiita.com/daxanya1/items/4709ad8454760e17148c

### sample_03.py

* PC接続されているカメラの映像を表示する
* 引数なし
* ↓を参考に
  http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

### sample_04.py

* カメラの映像を動画で保存する
  * m4v形式ファイルで保存される
  * 保存ファイル名は、ハードコーディング
  * 引数なし
* 参考
  http://qiita.com/daxanya1/items/4709ad8454760e17148c

### sample_05.py

* 動画をエッジ処理してみる
* 元動画とエッジ処理後の動画を二つ再生させる
  * 引数なし
* 参考
  http://qiita.com/daxanya1/items/4709ad8454760e17148c


### sample_06.py

* 静止画から顔検出してみる
* 画像ファイルはハードコーディング
* 参考
  http://www.takunoko.com/blog/python%E3%81%A7%E9%81%8A%E3%82%93%E3%81%A7%E3%81%BF%E3%82%8B-part1-opencv%E3%81%A7%E9%A1%94%E8%AA%8D%E8%AD%98/


### sample_07.py

* 動画ファイルから顔部分をくりぬいて、顔だけのファイルを作る
* 動画ファイルのパスはハードコーディング
* 参考
  http://hogehuga.com/post-241/

### sample_08.py

* 動画ファイルで顔認識する
* 参考
  http://www.takunoko.com/blog/python%E3%81%A7%E9%81%8A%E3%82%93%E3%81%A7%E3%81%BF%E3%82%8B-part1-opencv%E3%81%A7%E9%A1%94%E8%AA%8D%E8%AD%98/
* sample_08_2.py で動画再生しながら処理する

### sample_09.py

* Webカメラの映像を使って、リアルタイムで顔認識する
* 参考
  http://blanktar.jp/blog/2015/02/python-opencv-realtime-lauhgingman.html
  * このブログはけっこう参考になりそう

