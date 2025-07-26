from pkg_py.system_object.map_massages import PkMessages2025


def copy_except_blacklist(src_dir, dst_dir, exclude_names):

    """
    Copy files from src_dir to dst_dir excluding any files or directories
    whose names match those in exclude_names.

    Args:
        src_dir (str): Source directory.
        dst_dir (str): Destination directory.
        exclude_names (set): Set of names (files or folders) to exclude.
    """
    import os
    import shutil

    from pkg_py.functions_split.copy_except_blacklist import copy_except_blacklist
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


