#!/bin/bash

# 引数から週番号と課題番号を取得
week_number=$1
kadai_number=$2

# ディレクトリのパス
directory="/Users/pality/portfolio/KIC/python/kisoron"

# ファイル名を生成
filename="${directory}/week${week_number}-kadai${kadai_number}.py"

# ファイルが既に存在するかチェック
if [[ -f "$filename" ]]; then
    echo "Error: File '$filename' already exists."
else
    # ファイルが存在しない場合、生成
    touch "$filename"
    echo "Created file: $filename"
fi