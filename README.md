# CSVデータ可視化Streamlitアプリケーション

このリポジトリは、pyenvとpoetryを使用した開発環境の作成を練習するためのものです。
CSVファイルをアップロードして可視化するシンプルなStreamlitアプリケーションを含んでいます。

## プロジェクト概要

このアプリケーションでは、以下の機能を提供しています：
- CSVファイルのアップロード機能
- データプレビュー表示
- 特定カラム（estimated_retire_rate_normalized）のヒストグラム表示

## 環境構築

### 必要条件
- Python 3.11.6
- pyenv
- Poetry

### インストール手順

1. pyenvでPythonのバージョンを設定
```
pyenv install 3.11.6
pyenv local 3.11.6
```

2. Poetryを使った依存関係のインストール
```
poetry install
```

## アプリケーションの実行

以下のコマンドでStreamlitアプリを起動します：

```
poetry run streamlit run app.py
```

ブラウザで http://localhost:8501 を開くと、アプリケーションが表示されます。

## 使用方法

1. アプリケーションが起動したら、「hs_all.csvをアップロードしてください」という表示の下にあるボタンをクリックしてCSVファイルを選択します
2. アップロード後、データプレビューが表示されます
3. CSVファイルに「estimated_retire_rate_normalized」カラムが含まれている場合は、その分布がヒストグラムで表示されます

## 主な依存ライブラリ

- Streamlit: Webアプリケーションフレームワーク
- Pandas: データ処理と分析
- Matplotlib: データ可視化
- Seaborn: 統計データの可視化
