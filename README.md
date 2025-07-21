# 国土地理院 標高タイル（TXT）→ Mapbox Terrain-RGB 変換ツール

このツールは、国土地理院が提供する標高テキストタイル（`.txt`）をダウンロードし、Mapbox Terrain-RGB 形式の PNG タイル（`{z}/{x}/{y}.png`）に変換する Python スクリプトです。  
生成されたタイルは MapLibre GL JS や Mapbox GL JS 等での地形可視化に利用できます。

## 📌 概要

- **入力データ**：  
  国土地理院 DEM タイル  
  [https://cyberjapandata.gsi.go.jp/xyz/dem/{z}/{x}/{y}.txt](https://cyberjapandata.gsi.go.jp/xyz/dem/{z}/{x}/{y}.txt)

- **出力形式**：  
  Mapbox Terrain-RGB 形式の PNG タイル（`{z}/{x}/{y}.png`）

- **入力方式**：  
  `target.csv` に指定されたズーム・X・Y タイルのみ処理

- **グリッドサイズ**：  
  256 × 256

- **NoDataの扱い**：  
  標高 0m（RGB = `(1, 134, 160)`）として処理

## ✅ 特徴

- `target.csv` に記載されたタイルだけをピンポイントで処理可能
- 標高 `.txt` タイルを自動ダウンロード
- Terrain-RGB 形式で PNG に変換
- タイル階層 `{z}/{x}/{y}` に自動保存
- 処理中タイルをログで出力

## 🧰 必要なライブラリ

以下のパッケージを `pip` でインストールしてください：

```bash
pip install pillow requests
````

## 📂 `target.csv` のフォーマット

処理対象のタイルを以下の形式で記述してください：

```csv
z,x,y
1,1,0
2,3,1
3,6,3
...
```

## 🚀 使い方

1. `target.csv` をプロジェクトディレクトリに配置
2. スクリプトを実行：

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

出力された PNG は、以下の式に基づいて標高をエンコードしています：

```
標高 (m) = (R × 256 × 256 + G × 256 + B) × 0.1 - 10000
```

## 📝 注意点

* NoData（空欄または無効値）は標高 `0.0m` として処理され、RGB = `(1, 134, 160)` に変換されます。
* 日本国外のタイルや存在しないタイルにはアクセスできない場合があります。
* 通信状況によりダウンロードが失敗することがあります。

## 📄 ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。

> ※ 国土地理院のデータは「国土地理院コンテンツ利用規約」に基づいてご利用ください：
> [https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html](https://www.gsi.go.jp/kikakuchousei/kikakuchousei40182.html)

```