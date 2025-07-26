import os
from pkg_py.system_object.directories import D_FUNCTIONS_SPLIT, D_PKG_PY, D_REFACTOR, D_PK_SYSTEM_OBJECT


def ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str):
    d_target = os.path.abspath(d_target)

    if not os.path.isdir(d_target):
        print(f"[ERROR] 디렉토리 없음: {d_target}")
        return

    for root, dirs, files in os.walk(d_target):
        for filename in files:
            if not filename.endswith('.py'):
                continue  # .py 파일만 처리

            old_path = os.path.join(root, filename)
            modified = False

            # 파일 내용 수정
            try:
                with open(old_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                print(f"[SKIP] 바이너리 파일로 판단: {old_path}")
                continue

            if oldstr in content:
                new_content = content.replace(oldstr, new_str)
                with open(old_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"[MODIFIED CONTENT] {old_path}")
                modified = True

            # 파일명 변경
            if oldstr in filename:
                new_filename = filename.replace(oldstr, new_str)
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f"[RENAMED FILE] {old_path} → {new_path}")
                modified = True

            if not modified:
                print(f"[SKIP] 변경 없음: {old_path}")

# 사용 예시
if __name__ == "__main__":

    d_target = D_PKG_PY
    oldstr = "ensure_window_killed_by_title"
    new_str = "ensure_window_killed_by_title"
    ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str)

    d_target = D_FUNCTIONS_SPLIT
    ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str)

    d_target = D_REFACTOR
    ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str)

    # d_target = D_PK_SYSTEM_OBJECT
    # ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str)