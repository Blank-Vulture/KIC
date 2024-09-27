#!/bin/bash

# 1文字ずつ表示する関数
type_text() {
    local text="$1"
    local delay=0.05  # 表示間隔（秒）
    for (( i=0; i<${#text}; i++ )); do
        echo -n "${text:$i:1}"
        sleep $delay
    done
    echo
}

# 挨拶文
type_text "============================================"
type_text " こんにちは、学籍番号24024の白石鷹也です。"
type_text " プログラミング基礎論Pythonの最終課題のデモへようこそ！"
type_text "============================================"
echo
read -p ""

# 概要説明
type_text "本ツールはPythonファイルの静的解析とレポート生成を行います。"
type_text "解析結果は標準出力され、HTML形式のレポートとしても保存されます。"
echo
read -p ""

# ツールの基本的な使用方法説明
type_text "まず、ツールの基本的な使い方を確認します。"
type_text "以下のコマンドでヘルプメッセージを表示します。"
echo

# ヘルプメッセージの表示
type_text "   $ python3 verify.py -h"
read -p "Enter キーを押して、コマンドを実行します..."
python3 verify.py -h
echo
read -p ""

# ヘルプメッセージの説明
type_text "このヘルプメッセージには、ツールの使用方法や利用可能な引数が表示されます。"
type_text "引数には、ディレクトリの指定、レポートの保存、レポートの読み込み、"
type_text "さらに厳密モードでの解析を行うためのオプションが含まれています。"
echo
read -p ""

# ディレクトリ解析（通常モード）
type_text "次に、指定したディレクトリ 'week1' を解析します。"
type_text "ディレクトリを指定すると、その中のPythonファイルが解析されます。"
echo

# ディレクトリ解析
type_text "   $ python3 verify.py week1"
read -p "Enter キーを押して、コマンドを実行します..."
python3 verify.py week1
echo
read -p ""

# 厳密モード解析
type_text "次に、厳密モードで解析を行います。"
type_text "厳密モードでは、通常の解析に加えてさらに詳細なエラーや警告が報告されます。"
echo

# 厳密モード実行
type_text "   $ python3 verify.py --strict week1"
read -p "Enter キーを押して、コマンドを実行します..."
python3 verify.py --strict week1
echo
read -p ""

# JSONレポートの保存
type_text "次に、解析結果をJSON形式とhtmlレポート形式で保存します。"
type_text "これにより、解析結果のjsonファイルをほかのツールで使用することができます。"
echo

# JSON形式でレポート保存
type_text "   $ python3 verify.py --save-report"
read -p "Enter キーを押して、コマンドを実行します..."
python3 verify.py --save-report
echo
read -p "--------------------------------------------"

# JSONレポートの読み込み
type_text "保存されたレポートを読み込みます。"
type_text "この機能は、解析結果をもう一度チェックしたい時のためのものです。"
echo

# JSONレポートの読み込み
type_text "   $ python3 verify.py --load-report"
read -p "Enter キーを押して、コマンドを実行します..."
python3 verify.py --load-report
echo
read -p "--------------------------------------------"

# 複数引数の併用（ディレクトリ解析＋レポート保存）
type_text "次に、引数を組み合わせてディレクトリ解析とレポート保存を同時に行います。"
echo

# 引数の併用例
type_text "   $ python3 verify.py week1 --save-report"
read -p "Enter キーを押して、コマンドを実行します..."
python3 verify.py week1 --save-report
echo
read -p "--------------------------------------------"

# 複数引数の併用（厳密モード＋レポート保存）
type_text "次に、厳密モードでの解析とレポート保存を同時に行います。"
echo

# 厳密モード＋レポート保存
type_text "   $ python3 verify.py week1 --strict --save-report"
read -p "Enter キーを押して、コマンドを実行します..."
python3 verify.py week1 --strict --save-report
echo
read -p "--------------------------------------------"

# --load-reportと--strictの併用の警告説明
type_text "最後に、'--load-report' と '--strict' を併用した場合の警告を確認します。"
type_text "これらの引数は通常、同時に使用することが想定されておらず、"
type_text "併用すると警告が表示されます。"
echo

# --load-report＋--strict警告
type_text "   $ python3 verify.py --load-report --strict"
read -p "Enter キーを押して、コマンドを実行します..."
python3 verify.py --load-report --strict
echo
read -p "--------------------------------------------"

# デモ終了メッセージ
type_text "以上でデモを終了します。"
type_text "ご覧いただきありがとうございました！"