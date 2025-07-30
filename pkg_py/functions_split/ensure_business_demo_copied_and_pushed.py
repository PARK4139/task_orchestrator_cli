import os
import shutil

from pkg_py.functions_split.copy_except_blacklist import copy_except_blacklist


def     ensure_business_demo_copied_and_pushed():
    downloads_path = os.path.join(os.environ["USERPROFILE"], "Downloads")
    SOURCE_DIR = rf"{downloads_path}\pk_system"
    DEST_DIR = rf"{downloads_path}\business_demo"
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

    src = rf"{DEST_DIR}\.gitignore_for_making_business_demo_public"
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


