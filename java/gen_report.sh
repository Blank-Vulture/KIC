#!/bin/bash

# 引数で指定された期間のディレクトリ（period1, period2 など）と授業日を取得
PERIOD=$1
CLASS_DATE=$2

# 引数がない場合、使用方法を表示して終了
if [ -z "$PERIOD" ]; then
    echo "Usage: $0 <period-directory> [class-date (MM/DD or 'auto')]"
    exit 1
fi

# 授業日が"auto"と指定された場合、今週の金曜日を計算して設定
if [ "$CLASS_DATE" == "auto" ]; then
    TODAY=$(date +%u)
    if [ $TODAY -ge 6 ]; then
        CLASS_DATE=$(date -v-$(($TODAY - 5))d +"%m/%d")
    else
        CLASS_DATE=$(date -v+$(($((5 - $TODAY))))d +"%m/%d")
    fi
elif [ -z "$CLASS_DATE" ]; then
    CLASS_DATE=$(date +"%m/%d")
fi

# 基本パスの設定
SRC_DIR="/Users/pality/portfolio/KIC/java/tokuron/src/$PERIOD"
OUTPUT_DIR="./report"
REPORT_FILE="${OUTPUT_DIR}/${PERIOD}_report.md"

# ソースディレクトリが存在しない場合のエラーチェック
if [ ! -d "$SRC_DIR" ]; then
    echo "Error: Source directory '$SRC_DIR' does not exist."
    exit 1
fi

# reportディレクトリが存在しない場合は作成
if [ ! -d "$OUTPUT_DIR" ]; then
    mkdir -p "$OUTPUT_DIR"
fi

# レポートのタイトル、学籍番号、名前、授業日をMarkdown形式で作成
STUDENT_ID="24024"
STUDENT_NAME="白石鷹也"

# 期間番号を抽出し、整数として扱う
PERIOD_NUM=$(echo "$PERIOD" | grep -o -E '[0-9]+')
echo "# Java 課題レポート - 第${PERIOD_NUM}回" > $REPORT_FILE
echo "**学籍番号**: $STUDENT_ID" >> $REPORT_FILE
echo "**名前**: $STUDENT_NAME" >> $REPORT_FILE
echo "**授業日**: $CLASS_DATE" >> $REPORT_FILE
echo "" >> $REPORT_FILE

# 実行対象のファイルを検索し、Practice*.java、Mondai*.java の順で処理（昇順）
PRACTICE_FILES=$(find "$SRC_DIR" -name "Practice*.java" | sort)
MONDAI_FILES=$(find "$SRC_DIR" -name "Mondai*.java" | sort)

# サブディレクトリの検索（例: period2.Kadai1）
SUBDIRS=$(find /Users/pality/portfolio/KIC/java/tokuron/src -type d -name "$PERIOD.*" | sort)

# ファイルが見つからなかった場合のエラーチェック
if [ -z "$PRACTICE_FILES" ] && [ -z "$MONDAI_FILES" ] && [ -z "$SUBDIRS" ]; then
    echo "Warning: No Practice, Mondai files, or subdirectories found in '$SRC_DIR'."
fi

# Javaファイルのソースコードをレポートに追加する関数
add_to_report() {
    local file=$1
    local type=$2
    local display_number=$3
    local class_name=$(basename "$file" .java)
    local section_title="$type${display_number}-${class_name}"

    # ソースコードセクション
    echo "## $section_title" >> $REPORT_FILE
    echo "### ソースコード" >> $REPORT_FILE
    echo '```java' >> $REPORT_FILE
    echo >> $REPORT_FILE  # 改行を追加
    cat "$file" >> $REPORT_FILE
    echo >> $REPORT_FILE  # 改行を追加
    echo '```' >> $REPORT_FILE
    echo "" >> $REPORT_FILE

    # 実行結果セクション（手動で追加）
    echo "### 実行結果" >> $REPORT_FILE
    echo '```' >> $REPORT_FILE
    echo "（実行結果を貼り付けてください）" >> $REPORT_FILE
    echo '```' >> $REPORT_FILE
    echo "" >> $REPORT_FILE

    # ページブレークを追加
    echo '<div style="page-break-before:always"></div>' >> $REPORT_FILE
    echo "" >> $REPORT_FILE
}

# 各Practiceファイルをレポートに追加（昇順）
for file in $PRACTICE_FILES; do
    practice_num=$(basename "$file" .java | grep -o -E '[0-9]+')
    add_to_report "$file" "練習" $practice_num
done

# 各Mondaiファイルをレポートに追加（昇順）
for file in $MONDAI_FILES; do
    mondai_num=$(basename "$file" .java | grep -o -E '[0-9]+')
    add_to_report "$file" "問題" $mondai_num
done

# サブディレクトリの処理
for subdir in $SUBDIRS; do
    # サブディレクトリのタイトルを追加（例: period2.Kadai1）
    subdir_name=$(basename "$subdir")
    echo "## $subdir_name" >> $REPORT_FILE
    SUB_PRACTICE_FILES=$(find "$subdir" -name "Practice*.java" | sort)
    SUB_MONDAI_FILES=$(find "$subdir" -name "Mondai*.java" | sort)

    # サブディレクトリ内のファイルを追加
    for file in $SUB_PRACTICE_FILES; do
        practice_num=$(basename "$file" .java | grep -o -E '[0-9]+')
        add_to_report "$file" "練習" $practice_num
    done

    for file in $SUB_MONDAI_FILES; do
        mondai_num=$(basename "$file" .java | grep -o -E '[0-9]+')
        add_to_report "$file" "問題" $mondai_num
    done
done

# 備考セクションを追加
echo "## 備考" >> $REPORT_FILE
echo "eclipseを用いて課題を行いました。" >> $REPORT_FILE
echo "![eclipse](/Users/pality/portfolio/KIC/java/img/period${PERIOD_NUM}.png)" >> $REPORT_FILE

# 完了メッセージ
echo "${PERIOD}のレポートが '${REPORT_FILE}' として生成されました。"