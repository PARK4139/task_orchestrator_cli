import ast
import sys


def get_called_functions(file_path):
    """주어진 Python 파일에서 호출된 함수 목록을 추출"""
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)

    called_functions = set()

    # 함수 호출 탐색
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            called_functions.add(node.func.id)

    return called_functions


def remove_unused_functions(file_path):
    """사용되지 않는 함수들을 자동으로 제거"""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    tree = ast.parse("".join(lines), filename=file_path)
    called_functions = get_called_functions(file_path)

    new_lines = []
    inside_unused_function = False
    function_lines = []  # 제거할 함수의 라인 저장

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name not in called_functions:
                print(f"제거 대상: {node.name}()")
                function_lines.extend(range(node.lineno - 1, node.end_lineno))
            else:
                inside_unused_function = False

    # 실제 코드에서 제거 대상 함수의 라인을 제외
    for i, line in enumerate(lines):
        if i not in function_lines:
            new_lines.append(line)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python clean_functions.py <파일이름>")
        sys.exit(1)

    target_file = sys.argv[1]  # 사용할 Python 파일 입력
    remove_unused_functions(target_file)
