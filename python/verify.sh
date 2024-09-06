#!/bin/bash

# ベースディレクトリのパス
BASE_DIR="/Users/pality/portfolio/KIC/python"

# 成功、失敗、総ファイル数のカウンタ
success_count=0
error_count=0
total_count=0

# 一時ファイルにファイルリストを保存
file_list=$(mktemp)
find $BASE_DIR -name 'week*-kadai*.py' | sort -V > $file_list

# 一時ファイルからファイル名を読み込んでループ処理
while read script; do
    script_name=$(basename $script)
    echo -n "Running $script_name... "
    # スクリプトの実行結果を一時ファイルに保存
    OUTPUT=$(mktemp)
    python $script > $OUTPUT 2>&1
    if [ $? -eq 0 ]; then
        echo -e "\033[32mSuccess\033[0m"
        ((success_count++))
    else
        echo -e "\033[31mError occurred\033[0m"
        cat $OUTPUT  # エラーがあった場合、出力内容を表示
        ((error_count++))
    fi
    rm $OUTPUT  # 一時ファイルを削除
    ((total_count++))
done < $file_list

echo "Summary: Total $total_count Files, $success_count Success, $error_count Errors"

# 一時ファイルを削除
rm $file_list