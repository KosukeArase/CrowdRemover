# 素朴な質問

* get_configってなんで別でfunction書くの？

* ここってどうやってconfig渡ってんの？

```
    config = get_config()
    set_windows()

def set_windows():
    cv2.namedWindow(config.WINDOW_ORG)
    cv2.namedWindow(config.WINDOW_BACK)
    cv2.namedWindow(config.WINDOW_DIFF)
```

* `_flag = _out.open(FILE_ORG.split(".")[0]+".avi"`ってなんで拡張子変えてんの？ movだと保存できない感じか．なるほど．

# cv2

## videoオブジェクト

[参考](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_gui/py_video_display/py_video_display.html)

#### 動画読込オブジェクト: cap = cv2.VideoCapture()

* 動画ファイル名，カメラの番号を引数に．

#### フレーム読み込み：cap.read() 

* (True/False)の2値の値を返します．フレームの読み込みが正しく行われれば True を返すので，この関数の返戻値によって動画ファイルの最後まで到達したかどうかを確認できます
* capが初期化してないとエラー．cap.isOpened()で確認できる．


## 背景差分　cv2.createBackgroundSubtractorMOG2

[参考](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_video/py_bg_subtraction/py_bg_subtraction.html#backgroundsubtractormog2)

#### 1. cv2.createBackgroundSubtractorMOG

* 混合正規分布を基にした前景・背景の領域分割アルゴリズム
* 背景に属する各画素を混合数が3から5の混合分布でモデル化
* 混合分布の重みはシーン中に対応する色が存在している時間の割合．可能性の高い背景色は長く留まり，より静的になります．
* P. KadewTraKuPongとR. Bowden, 2001 “An improved adaptive background mixture model for real-time tracking with shadow detection” 

#### 2. cv2.createBackgroundSubtractorMOG2

* 混合正規分布を基にした前景・背景の領域分割アルゴリズム
* このアルゴリズムの重要な点は，画素毎に最適な混合数を選択する点
* 照明の変化などといった動的なシーンに対する適応力が優れています
* Z.Zivkovic 2004, “Improved adaptive Gausian mixture model for background subtraction” 2006年, “Efficient Adaptive Density Estimation per Image Pixel for the Task of Background Subtraction” 


#### 3. cv2.BackgroundSubtractorGMG

* 統計的な背景の推定法と画素単位でのベイス推定に基づく領域分割を組み合わせたアルゴリズム
* Andrew B. Godbehere, Akihiro Matsukawa, Ken Goldberg 2012, “Visual Tracking of Human Visitors under Variable-Lighting Conditions for a Responsive Audio Art Installation”
* 背景のモデル構築に最初の数フレーム(デフォルトで120)を使用．ベイズ推定を使って前景物体である可能性を識別する確率的前景領域抽出アルゴリズムを使用．
*  推定は適応的であり，照明変化に対する適応力を上げるために，古い画像より新しい画像を重視．
* クロージングやオープニングといったモーフォロジカル処理を行いノイズを削除します．最初の数フレームの間は背景モデルを作成するため，真っ黒なウィンドウが表示される．

## モルフォロジー変換

[参考](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html)

基本的処理

* Erosion: 2dconvのようなフィルタ，フィルタ中の全ての値が'1'のときのみ'1'とすることで実現．
* Delation: 膨張はその逆．１つでも'1'があれば．

組合せ処理

* opening
* closing

カーネル

* 矩形，楕円形，十字型

`cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))`

## 輪郭

[参考](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html)

#### `cv2.findContours()`

* 入力画像を破壊的に変換するので，事前にコピーが必要．
* 物体は白,背景は黒

`image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)`

* thresh: バイナリ画像
* 第二引数: contour retrieval mode
* 第三引数: 輪郭検出方法．すべての座標を保持する必要が無いから近似してやろうぜ的なやつのオプション
* 出力は輪郭画像，輪郭(検出された全輪郭をPythonのlist)，輪郭の階層情報

`img = cv2.drawContours(img, contours, -1, (0,255,0), 3)`	

## 輪郭の特徴

[参考](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html)

### 外接矩形

`cv2.boundingRect()`

* 回転を考慮したものもある．`cv2.minAreaRect() `
