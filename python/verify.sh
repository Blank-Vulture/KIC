#!/bin/bash

# Python スクリプトが保存されているディレクトリ
DIRECTORY="/Users/pality/portfolio/KIC/python"

# 成功、失敗、総ファイル数のカウンタ
success_count=0
error_count=0
total_count=0

# ディレクトリ内のすべての .py ファイルに対してループ処理
for script in $DIRECTORY/*.py; do
    script_name=$(basename $script)
    echo -n "Running $script_name... "
    # スクリプトの実行結果を一時ファイルに保存
    OUTPUT=$(mktemp)
    python $script > $OUTPUT 2>&1
    if [ $? -eq 0 ]; then
        echo -e "\033[32m$script_name: Success\033[0m"
        ((success_count++))
    else
        echo -e "\033[31m$script_name: Error occurred\033[0m"
        cat $OUTPUT  # エラーがあった場合、出力内容を表示
        ((error_count++))
    fi
    rm $OUTPUT  # 一時ファイルを削除
    ((total_count++))
done

echo "Summary: Total $total_count Files, $success_count Success, $error_count Errors"