import os
import shutil

from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.map_massages import PkMessages2025


def copy_except_blacklist(src_dir, dst_dir, exclude_names):
    """
    Copy files from src_dir to dst_dir excluding any files or directories
    whose names match those in exclude_names.

    Args:
        src_dir (str): Source directory.
        dst_dir (str): Destination directory.
        exclude_names (set): Set of names (files or folders) to exclude.
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    copied_count = 0
    for root, dirs, files in os.walk(src_dir):
        # 디렉토리 제외
        dirs[:] = [d for d in dirs if d not in exclude_names]
        # 파일 복사
        for file in files:
            if file in exclude_names:
                continue

            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, src_dir)
            dst_path = os.path.join(dst_dir, rel_path)

            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)
            print(f"[COPIED] {rel_path}")
            copied_count += 1

    print(f"[{PkMessages2025.DONE}] {copied_count} file(s) copied to '{dst_dir}'.")


if __name__ == "__main__":
    downloads_path = os.path.join(os.environ["USERPROFILE"], "Downloads")
    SOURCE_DIR = rf"{downloads_path}\pk_system"
    DEST_DIR = rf"{downloads_path}\auto_utility"
    EXCLUDE_NAMES = {
        # 제외할 파일/디렉토리 이름
        "__pycache__",
        ".git",
        ".venv",
        ".gitignore",
        "pk_system.egg-info",
        ".idea",
        "# .gitignore",
    }
    copy_except_blacklist(SOURCE_DIR, DEST_DIR, EXCLUDE_NAMES)

    src = rf"{DEST_DIR}\.gitignore_for_public"
    dst = rf"{DEST_DIR}\.gitignore"
    try:
        if os.path.exists(dst):
            os.remove(dst)  # 덮어쓰기
        shutil.move(src, dst)  # 이동 및 이름 변경
        print(f"[OK] Overwritten:\n{src}\n→ {dst}")
    except FileNotFoundError:
        print(f"[ERROR] Source file not found: {src}")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

    os.chdir(path=DEST_DIR)
    # os.system(command=rf"call {DEST_DIR}\pk_push_project_to_github.bat")
    os.system(command=rf"call {DEST_DIR}\pk_push_project_to_github_hybrid.bat")
