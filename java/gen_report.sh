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
SRC_DIR="/Users/pality/portfolio/KIC/java/tokuron/src"
OUTPUT_DIR="./report"
REPORT_FILE="${OUTPUT_DIR}/${PERIOD}_report.md"

# ソースディレクトリが存在しない場合のエラーチェック
if [ ! -d "$SRC_DIR/$PERIOD" ]; then
    echo "Error: Source directory '$SRC_DIR/$PERIOD' does not exist."
    exit 1
fi

# reportディレクトリが存在しない場合は作成
if [ ! -d "$OUTPUT_DIR" ];then
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

# 指定されたperiodディレクトリ以下のすべてのJavaファイルを検索（再帰的に）
ALL_FILES=$(find "$SRC_DIR/$PERIOD" -type f -name "*.java" | sort)

# ファイルが見つからなかった場合のエラーチェック
if [ -z "$ALL_FILES" ]; then
    echo "Warning: No Java files found in '$SRC_DIR/$PERIOD'."
fi

# Javaファイルのソースコードをレポートに追加する関数
add_to_report() {
    local file=$1
    local section_title=$2
    local class_name=$(basename "$file" .java)

    # ソースコードセクション
    echo "## $section_title" >> $REPORT_FILE
    echo "### ソースコード" >> $REPORT_FILE
    echo '```java' >> $REPORT_FILE
    cat "$file" >> $REPORT_FILE
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

# 練習と課題の表示フラグを初期化
FIRST_PRACTICE_ADDED=false
FIRST_KADAI_ADDED=false

# すべてのJavaファイルを処理
for file in $ALL_FILES; do
    class_name=$(basename "$file" .java)
    parent_dir=$(basename "$(dirname "$file")")

    # ファイル名または親ディレクトリ名で「練習」か「課題」かを判定
    if [[ $class_name =~ Practice ]] || [[ $parent_dir =~ practice ]]; then
        # 最初の練習セクションの追加
        if [ "$FIRST_PRACTICE_ADDED" = false ]; then
            echo "## 練習" >> $REPORT_FILE
            FIRST_PRACTICE_ADDED=true
        fi
        practice_num=$(echo "$class_name" | grep -o -E '[0-9]+')
        if [ -z "$practice_num" ]; then
            practice_num="10" # practice10 の場合
        fi
        add_to_report "$file" "練習${practice_num}"
    else
        # 最初の課題セクションの追加
        if [ "$FIRST_KADAI_ADDED" = false ]; then
            echo "## 課題" >> $REPORT_FILE
            FIRST_KADAI_ADDED=true
        fi
        mondai_num=$(echo "$class_name" | grep -o -E '[0-9]+')
        add_to_report "$file" "問題${mondai_num}"
    fi
done

# 備考セクションを追加
echo "## 備考" >> $REPORT_FILE
echo "eclipseを用いて課題を行いました。" >> $REPORT_FILE
echo "![eclipse](/Users/pality/portfolio/KIC/java/img/period${PERIOD_NUM}.png)" >> $REPORT_FILE

# 完了メッセージ
echo "${PERIOD}のレポートが '${REPORT_FILE}' として生成されました。"