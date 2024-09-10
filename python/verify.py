import subprocess
import os
import re
import time

# 色の設定
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def natural_sort_key(text):
    """文字列から数値を抽出し、自然順でソートするためのキーを返す。"""
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', text)]

def format_all_scripts(base_directory):
    # 'week' で始まるディレクトリを自動検出し、数値順にソート
    directories_to_check = sorted(
        [d for d in os.listdir(base_directory) if re.match(r'^week\d+', d)],
        key=natural_sort_key
    )

    # 対象ディレクトリ内の全てのPythonファイルのリストを取得
    python_files = []
    for directory in directories_to_check:
        full_path = os.path.join(base_directory, directory)
        for root, dirs, files in os.walk(full_path):
            sorted_files = sorted(
                [file for file in files if file.endswith('.py')],
                key=natural_sort_key
            )
            for file in sorted_files:
                python_files.append(os.path.join(root, file))

    # Blackで一括フォーマット
    if python_files:
        print("Formatting all scripts with Black...")
        subprocess.run(['black'] + python_files, check=True)

def run_static_analysis(base_directory):
    # 'week' で始まるディレクトリを自動検出し、数値順にソート
    directories_to_check = sorted(
        [d for d in os.listdir(base_directory) if re.match(r'^week\d+', d)],
        key=natural_sort_key
    )

    report = []
    success_count = 0
    fail_count = 0
    total_count = 0

    for directory in directories_to_check:
        full_path = os.path.join(base_directory, directory)
        print(f"Analyzing scripts in {full_path}...")
        for root, dirs, files in os.walk(full_path):
            sorted_files = sorted(
                [file for file in files if file.endswith('.py')],
                key=natural_sort_key
            )
            for file in sorted_files:
                file_path = os.path.join(root, file)
                total_count += 1

                # 各ツールの出力を一時ファイルに保存
                pylint_output = run_tool(['pylint', file_path], 'PyLint')
                ruff_output = run_tool(['ruff', 'check', file_path], 'Ruff')
                mypy_output = run_tool(['mypy', file_path], 'Mypy')

                # エラーがある場合のみレポートに追加
                if "error" in pylint_output.lower() or "error" in ruff_output.lower() or "error" in mypy_output.lower() or \
                        "warning" in pylint_output.lower() or "warning" in ruff_output.lower() or "warning" in mypy_output.lower():
                    print(f"{RED}Fail{RESET} - {file_path}")
                    report.append({
                        'file': file_path,
                        'pylint': pylint_output,
                        'ruff': ruff_output,
                        'mypy': mypy_output
                    })
                    fail_count += 1
                else:
                    print(f"{GREEN}Success{RESET} - {file_path}")
                    success_count += 1

    # レポートをまとめて表示
    summarize_report(report, total_count, success_count, fail_count)

def run_tool(command, tool_name):
    result = subprocess.run(command, text=True, capture_output=True)
    output = ""
    if result.stdout:
        output += result.stdout
    if result.stderr:
        output += result.stderr

    return output.strip()

def summarize_report(report, total_count, success_count, fail_count):
    print("\nSummary Report\n" + "="*40)
    if not report:
        print("All checks passed without any errors.")
    for entry in report:
        print(f"\nFile: {entry['file']}\n" + "-"*40)
        print(f"PyLint Results:\n{entry['pylint']}")
        print(f"Ruff Results:\n{entry['ruff']}")
        print(f"Mypy Results:\n{entry['mypy']}")
        print("-"*40)
    print("\nEnd of Report\n")
    print(f"Total: {total_count}, {GREEN}Success: {success_count}{RESET}, {RED}Fail: {fail_count}{RESET}")

# ベースディレクトリのパスを指定
base_directory = "/Users/pality/portfolio/KIC/python"

# 開始時間の記録
start_time = time.time()

format_all_scripts(base_directory)  # 最初に全てのスクリプトを一括でフォーマット
run_static_analysis(base_directory)  # その後、静的解析を実行

# 終了時間の記録と処理時間の表示
end_time = time.time()
process_time = end_time - start_time
print(f"Process Time: {process_time:.2f} seconds")