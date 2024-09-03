#!/bin/bash

# 圧縮するディレクトリのパスを指定
DIRECTORY="/Users/pality/portfolio/KIC/python/kisoron"

# ディレクトリに移動
cd "$DIRECTORY"

# 既存のすべてのZIPファイルを削除
rm -f week*-kadai.zip

# ファイル名からすべての週番号を取得し、ユニークな週番号のリストを作成
weeks=($(ls week*-kadai*.py 2>/dev/null | grep -o 'week[0-9]\+' | sort -u))

# ユニークな週番号ごとに処理
for week in "${weeks[@]}"
do
    # ZIPファイル名を生成
    ZIP_FILE="${week}-kadai.zip"

    # 特定の週のPythonファイルをZIP形式で圧縮
    zip -j "$ZIP_FILE" "${week}-kadai*.py"
done

echo "All Python files have been appropriately zipped into their respective week archives."