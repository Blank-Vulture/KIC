#!/bin/bash

# 基本ディレクトリ
BASE_DIR="/Users/pality/portfolio/KIC/python"

# 圧縮ファイルを保存するディレクトリ
ZIP_DIR="$BASE_DIR/submission"

# 既存のZIPファイルを削除
rm -f "$ZIP_DIR"/*.zip

# 各週のディレクトリを検索してZIP圧縮
for week_folder in $BASE_DIR/week*
do
    week=$(basename $week_folder)
    zip_file="$ZIP_DIR/${week}-kadai.zip"
    # 圧縮コマンド（ディレクトリ構造を無視）
    zip -j "$zip_file" "$week_folder"/*.py
done

echo "All Python files have been appropriately zipped into their respective week archives in $ZIP_DIR."