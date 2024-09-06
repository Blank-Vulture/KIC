#!/bin/bash

# ベースディレクトリのパス
BASE_DIR="/Users/pality/portfolio/KIC/python"

# 週番号をコマンドライン引数から取得（例：1）
WEEK_NUM=$1

# 課題番号をコマンドライン引数から取得（例：1）
KADAI_NUM=$2

# ディレクトリ名の生成（例：week1）
WEEK_DIR="${BASE_DIR}/week${WEEK_NUM}"

# ファイル名の生成（例：week1-kadai1.py）
FILE_NAME="week${WEEK_NUM}-kadai${KADAI_NUM}.py"

# 指定された週のディレクトリがなければ作成
if [ ! -d "$WEEK_DIR" ]; then
    mkdir "$WEEK_DIR"
    echo "Created directory: $WEEK_DIR"
fi

# 指定されたPythonファイルを作成（ファイルが存在しない場合）
FILE_PATH="${WEEK_DIR}/${FILE_NAME}"
if [ ! -f "$FILE_PATH" ]; then
    touch "$FILE_PATH"
    echo "Created file: $FILE_PATH"
else
    echo "File already exists: $FILE_PATH"
fi