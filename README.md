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

