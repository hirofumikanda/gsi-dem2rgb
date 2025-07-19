# 国土地理院 標高タイル（TXT）→ Mapbox Terrain-RGB 変換ツール

このツールは、国土地理院が提供する標高テキストタイル（`.txt`）をダウンロードし、Mapbox Terrain-RGB 形式の PNG タイル（`{z}/{x}/{y}.png`）に変換する Python スクリプトです。生成されたタイルは MapLibre GL JS や Mapbox GL JS 等での地形可視化に利用できます。

## 📌 概要

- **入力データ**：  
  国土地理院 DEM タイル（[https://cyberjapandata.gsi.go.jp/xyz/dem/{z}/{x}/{y}.txt](https://cyberjapandata.gsi.go.jp/xyz/dem/{z}/{x}/{y}.txt)）

- **出力形式**：  
  Mapbox Terrain-RGB 形式の PNG タイル（`{z}/{x}/{y}.png`）

- **対応ズームレベル**：  
  z=1〜14

- **グリッドサイズ**：  
  256 × 256

- **NoDataの扱い**：  
  標高 0m（RGB = `(1, 134, 160)`）として処理

## ✅ 特徴

- 日本国内のタイル座標範囲を自動で取得
- 標高 `.txt` タイルをダウンロード
- Mapbox Terrain-RGB 形式で PNG に変換
- タイル階層 `{z}/{x}/{y}` に自動保存
- 処理中のタイルをログ出力

## 🧰 必要なライブラリ

以下のパッケージを `pip` でインストールしてください：

```bash
pip install pillow requests mercantile
````

## 🚀 使い方

以下のスクリプトを実行することで、タイルのダウンロードと変換が行われます：

```bash
python main.py
```

出力ファイル構造の例：

```
dem_txt/
└── 14/
    └── 14600/
        └── 6480.txt

terrain_rgb/
└── 14/
    └── 14600/
        └── 6480.png
```

## 🗺️ Terrain-RGB 形式について

出力された PNG は、次の式に基づいて標高をエンコードしています：

```
標高 (m) = (R × 256 × 256 + G × 256 + B) × 0.1 - 10000
```

## 📝 注意点

* NoData（空欄または無効値）は標高 `0.0m` として処理され、RGB = `(1, 134, 160)` に変換されます。
* ログは標準出力またはファイル（オプション）に出力可能です。

## 📄 ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。

> ※ 国土地理院のデータは「国土地理院コンテンツ利用規約」に基づいてご利用ください：
> [https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)
