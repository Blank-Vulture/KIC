import subprocess
import os
import re
import time
import json
import webbrowser
import jinja2
import matplotlib.pyplot as plt
from argparse import ArgumentParser

# 色の設定
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

def natural_sort_key(text):
    """文字列から数値を抽出し、自然順でソートするためのキーを返す。"""
    return [int(t) if t.isdigit() else t for t in re.split(r'(\d+)', text)]

class Analyzer:
    def __init__(self, base_directory, strict_mode=False, specific_directory=None):
        self.base_directory = base_directory
        self.specific_directory = specific_directory
        self.strict_mode = strict_mode
        self.directories_to_check = self._get_directories() if not specific_directory else []
        self.python_files = []
        self.report = []
        self.summary = {
            'total_files': 0,
            'success': 0,
            'fail': 0,
            'total_errors': 0,
            'total_warnings': 0,
            'total_suggestions': 0,
            'process_time': 0
        }

    def _get_directories(self):
        """チェック対象のディレクトリを取得（ディレクトリ指定なしの場合）"""
        directories = sorted(
            [d for d in os.listdir(self.base_directory) if re.match(r'^week\d+', d)],
            key=natural_sort_key
        )
        print(f"Found directories: {directories}")  # デバッグ出力
        return directories

    def collect_python_files(self):
        """Pythonファイルを収集"""
        if self.specific_directory:
            # 特定のディレクトリが指定された場合、そのディレクトリ内の全ての.pyファイルを探索
            for root, dirs, files in os.walk(self.specific_directory):
                sorted_files = sorted(
                    [file for file in files if file.endswith('.py')],
                    key=natural_sort_key
                )
                for file in sorted_files:
                    self.python_files.append(os.path.join(root, file))
        else:
            # ディレクトリ指定がない場合、現在の探索アルゴリズムを使用
            index = 0
            while index < len(self.directories_to_check):
                directory = self.directories_to_check[index]
                full_path = os.path.join(self.base_directory, directory)
                for root, dirs, files in os.walk(full_path):
                    sorted_files = sorted(
                        [file for file in files if file.endswith('.py')],
                        key=natural_sort_key
                    )
                    for file in sorted_files:
                        self.python_files.append(os.path.join(root, file))
                index += 1

    def format_files_with_black(self):
        """各PythonファイルをBlackで自動整形"""
        for file_path in self.python_files:
            try:
                subprocess.run(['black', file_path], check=True)
                print(f"Formatted {file_path} with black.")
            except subprocess.CalledProcessError as e:
                print(f"Error formatting {file_path} with black: {e}")

    def run_analysis(self):
        """静的解析を実行"""
        self.collect_python_files()
        if not self.python_files:
            print("No Python files found.")
            return

        # ここで各ファイルをBlackで自動整形
        self.format_files_with_black()

        start_time = time.time()

        for file_path in self.python_files:
            self.summary['total_files'] += 1
            pylint_data = self._run_tool(['pylint', file_path] + (['--disable=all', '--enable=error'] if self.strict_mode else []), 'PyLint')
            ruff_data = self._run_tool(['ruff', 'check', file_path] + (['--select=ALL'] if self.strict_mode else []), 'Ruff')
            mypy_data = self._run_tool(['mypy', file_path], 'Mypy')

            file_errors = len(pylint_data['errors']) + len(ruff_data['errors']) + len(mypy_data['errors'])
            file_warnings = len(pylint_data['warnings']) + len(ruff_data['warnings']) + len(mypy_data['warnings'])
            file_suggestions = len(pylint_data['suggestions']) + len(ruff_data['suggestions']) + len(mypy_data['suggestions'])

            self.summary['total_errors'] += file_errors
            self.summary['total_warnings'] += file_warnings
            self.summary['total_suggestions'] += file_suggestions

            if file_errors > 0 or file_warnings > 0:
                print(f"{RED}Fail{RESET} - {file_path}")
                self.report.append({
                    'file': file_path,
                    'pylint': pylint_data,
                    'ruff': ruff_data,
                    'mypy': mypy_data
                })
                self.summary['fail'] += 1
            else:
                print(f"{GREEN}Success{RESET} - {file_path}")
                self.summary['success'] += 1

        self.summary['process_time'] = f"{time.time() - start_time:.2f} seconds"
        self.summarize_report()

    def _run_tool(self, command, tool_name):
        """静的解析ツールの実行と結果の解析"""
        try:
            result = subprocess.run(command, text=True, capture_output=True)
            output = result.stdout + result.stderr
            return self._parse_output(output)
        except subprocess.CalledProcessError as e:
            print(f"Error running {tool_name}: {e}")
            return {'errors': [], 'warnings': [], 'suggestions': []}

    def _parse_output(self, output):
        """出力の解析"""
        errors = []
        warnings = []
        suggestions = []

        lines = output.splitlines()
        for line in lines:
            if 'error' in line.lower():
                errors.append(line)
            elif 'warning' in line.lower():
                warnings.append(line)
            else:
                suggestions.append(line)

        return {
            'errors': errors,
            'warnings': warnings,
            'suggestions': suggestions
        }

    def summarize_report(self):
        """解析結果を表示"""
        print("\nSummary Report\n" + "=" * 40)
        if not self.report:
            print("All checks passed without any errors.")
        for entry in self.report:
            print(f"\nFile: {entry['file']}\n" + "-" * 40)
            print(f"PyLint Results:\n{entry['pylint']}")
            print(f"Ruff Results:\n{entry['ruff']}")
            print(f"Mypy Results:\n{entry['mypy']}")
            print("-" * 40)
        print("\nEnd of Report\n")
        print(f"Total: {self.summary['total_files']}, {GREEN}Success: {self.summary['success']}{RESET}, {RED}Fail: {self.summary['fail']}{RESET}")

class AdvancedAnalyzer(Analyzer):
    def __init__(self, base_directory, strict_mode=False, specific_directory=None, new_attribute=None):
        super().__init__(base_directory, strict_mode, specific_directory)
        self.new_attribute = new_attribute

class ReportGenerator:
    def __init__(self, report_data):
        self.report_data = report_data

    def save_report(self, json_path):
        """レポートをJSON形式で保存"""
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, 'w') as f:
            json.dump(self.report_data, f, indent=4)
        print(f"Report saved to {json_path}")

    def load_report(self, json_path):
        """レポートをJSONファイルから読み込む"""
        with open(json_path, 'r') as f:
            self.report_data = json.load(f)

    def generate_html_report(self):
        """HTMLレポートを生成してブラウザで表示"""
        template = """
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <title>解析レポート</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                .error { color: #dc3545; }
                .warning { color: #ff8c00; }
                .suggestion { color: #28a745; }
                .code-block {
                    background-color: #f8f9fa;
                    padding: 10px;
                    border-radius: 5px;
                    font-family: monospace;
                    white-space: pre-wrap;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="mt-4">解析レポート</h1>
                <p>総ファイル数: {{ report.summary.total_files }}</p>
                <p>成功: {{ report.summary.success }}</p>
                <p>失敗: {{ report.summary.fail }}</p>
                <p>処理時間: {{ report.summary.process_time }}</p>

                <h2 class="mt-4">エラー、警告、提案の比率</h2>
                <img src="report_chart.png" class="img-fluid" alt="Error, Warning, and Suggestion Ratio">

                <h2 class="mt-4">ファイル別結果</h2>
                {% for file in report.files %}
                <div class="card mt-3">
                    <div class="card-header">
                        {{ file.file }}
                    </div>
                    <ul class="list-group list-group-flush">
                        {% if file.pylint.errors %}
                        <li class="list-group-item error">
                            <strong>PyLint エラー</strong>
                            <ul>
                            {% for error in file.pylint.errors %}
                                <li class="code-block">{{ error }}</li>
                            {% endfor %}
                            </ul>
                        </li>
                        {% endif %}
                        {% if file.pylint.warnings %}
                        <li class="list-group-item warning">
                            <strong>PyLint 警告</strong>
                            <ul>
                            {% for warning in file.pylint.warnings %}
                                <li class="code-block">{{ warning }}</li>
                            {% endfor %}
                            </ul>
                        </li>
                        {% endif %}
                        {% if file.ruff.errors %}
                        <li class="list-group-item error">
                            <strong>Ruff エラー</strong>
                            <ul>
                            {% for error in file.ruff.errors %}
                                <li class="code-block">{{ error }}</li>
                            {% endfor %}
                            </ul>
                        </li>
                        {% endif %}
                        {% if file.ruff.warnings %}
                        <li class="list-group-item warning">
                            <strong>Ruff 警告</strong>
                            <ul>
                            {% for warning in file.ruff.warnings %}
                                <li class="code-block">{{ warning }}</li>
                            {% endfor %}
                            </ul>
                        </li>
                        {% endif %}
                        {% if file.ruff.suggestions %}
                        <li class="list-group-item suggestion">
                            <strong>Ruff 提案</strong>
                            <ul>
                            {% for suggestion in file.ruff.suggestions %}
                                <li class="code-block">{{ suggestion }}</li>
                            {% endfor %}
                            </ul>
                        </li>
                        {% endif %}
                        {% if file.mypy.errors %}
                        <li class="list-group-item error">
                            <strong>Mypy エラー</strong>
                            <ul>
                            {% for error in file.mypy.errors %}
                                <li class="code-block">{{ error }}</li>
                            {% endfor %}
                            </ul>
                        </li>
                        {% endif %}
                        {% if file.mypy.warnings %}
                        <li class="list-group-item warning">
                            <strong>Mypy 警告</strong>
                            <ul>
                            {% for warning in file.mypy.warnings %}
                                <li class="code-block">{{ warning }}</li>
                            {% endfor %}
                            </ul>
                        </li>
                        {% endif %}
                        {% if file.mypy.suggestions %}
                        <li class="list-group-item suggestion">
                            <strong>Mypy 提案</strong>
                            <ul>
                            {% for suggestion in file.mypy.suggestions %}
                                <li class="code-block">{{ suggestion }}</li>
                            {% endfor %}
                            </ul>
                        </li>
                        {% endif %}
                    </ul>
                </div>
                {% endfor %}
            </div>
        </body>
        </html>
        """
        template_env = jinja2.Environment(loader=jinja2.BaseLoader)
        html_content = template_env.from_string(template).render(report=self.report_data)
        output_dir = 'AnalyticsReport'
        os.makedirs(output_dir, exist_ok=True)
        html_path = os.path.join(output_dir, 'report.html')
        with open(html_path, 'w') as f:
            f.write(html_content)
        webbrowser.open('file://' + os.path.realpath(html_path))

    def draw_charts(self):
        """エラー、警告、提案の比率を示すチャートを生成"""
        total_errors = self.report_data['summary']['total_errors']
        total_warnings = self.report_data['summary']['total_warnings']
        total_suggestions = self.report_data['summary']['total_suggestions']

        labels = ['Errors', 'Warnings', 'Suggestions']
        values = [total_errors, total_warnings, total_suggestions]
        colors = ['#ff4c4c', '#ff8c00', '#28a745']  # 警告の色をオレンジに変更

        plt.figure(figsize=(8, 4))
        plt.barh(labels, values, color=colors)
        plt.title('Error, Warning, and Suggestion Ratio')
        plt.xlabel('Count')
        plt.ylabel('Type')

        output_dir = 'AnalyticsReport'
        os.makedirs(output_dir, exist_ok=True)
        chart_path = os.path.join(output_dir, 'report_chart.png')

        try:
            plt.savefig(chart_path)
            print(f"Chart saved to {chart_path}")
        except Exception as e:
            print(f"Failed to save the chart: {e}")
        plt.close()

def main():
    parser = ArgumentParser(description="File analysis and reporting tool")
    parser.add_argument('--save-report', action='store_true', help='Save analysis report to report.json')
    parser.add_argument('--load-report', action='store_true', help='Load analysis from report.json and generate HTML report')
    parser.add_argument('--strict', action='store_true', help='Run analysis in strict mode')
    parser.add_argument('directory', nargs='?', default=None, help='Directory to analyze')

    args = parser.parse_args()

    # ディレクトリが指定されていればそのディレクトリ内の.pyファイルを探索
    if args.directory:
        print(f"Analyzing specified directory: {args.directory}")
        analyzer = AdvancedAnalyzer(base_directory='.', specific_directory=args.directory, strict_mode=args.strict)
    else:
        print(f"Analyzing base directory: .")
        analyzer = AdvancedAnalyzer(base_directory='.', strict_mode=args.strict)

    if args.load_report:
        if args.strict:
            print(f"{RED}--strict is ignored when used with --load-report.{RESET}")
        report_generator = ReportGenerator({})
        report_generator.load_report(os.path.join('AnalyticsReport', 'report.json'))  # Load the report data
        report_generator.draw_charts()
        report_generator.generate_html_report()
    elif args.save_report:
        analyzer.run_analysis()
        report_generator = ReportGenerator({
            'files': analyzer.report,
            'summary': analyzer.summary
        })
        report_generator.save_report(os.path.join('AnalyticsReport', 'report.json'))
        report_generator.draw_charts()
        report_generator.generate_html_report()
    else:
        analyzer.run_analysis()

if __name__ == '__main__':
    main()