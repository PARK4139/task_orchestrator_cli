import logging


def ensure_filename_and_file_content_text_replaced_advanced(d_target, old_text, new_text, target_extensions=None, ignored_directory_names=None):
    import os
    import traceback
    from pathlib import Path

    from sources.functions.ensure_filename_and_file_content_text_replaced import ensure_filename_and_file_content_text_replaced_core
    from sources.objects.pk_local_test_activate import LTA
    if target_extensions is None:
        target_extensions = []
    if ignored_directory_names is None:
        ignored_directory_names = []

    d_target_path = Path(d_target).resolve()
    logging.debug(f'd_target={d_target_path} {"%%%FOO%%%" if LTA else ""}')

    if not d_target_path.is_dir():
        logging.debug(f"[ERROR] 디렉토리 없음: {d_target_path}")
        return

    dirs_to_rename = []

    # Step 1: Walk the directory tree from the bottom up, process files, and collect directory rename tasks.
    for root, dirs, files in os.walk(str(d_target_path), topdown=False):
        # Process files (rename and content replacement)
        for filename in files:
            file_path_old = Path(root) / filename
            
            if target_extensions and not any(str(file_path_old).lower().endswith(ext) for ext in target_extensions):
                continue

            if ignored_directory_names and any(ignored_dir in str(file_path_old) for ignored_dir in ignored_directory_names):
                # logging.debug()(f"[SKIP] Ignored directory name found in path: {file_path_old}")
                continue
            
            ensure_filename_and_file_content_text_replaced_core(f_target=str(file_path_old), old_text=old_text, new_text=new_text)

        # Collect directories to rename
        for dir_name in dirs:
            dir_path_old = Path(root) / dir_name

            if ignored_directory_names and any(ignored_dir in str(dir_path_old) for ignored_dir in ignored_directory_names):
                continue

            if old_text in dir_name:
                new_dir_name = dir_name.replace(old_text, new_text)
                dir_path_new = Path(root) / new_dir_name
                dirs_to_rename.append((str(dir_path_old), str(dir_path_new)))

    # Step 2: Rename the collected directories after the walk is complete.
    # Sort by path length (depth) in descending order to rename deepest directories first.
    dirs_to_rename.sort(key=lambda x: len(x[0]), reverse=True)

    for dir_path_old, dir_path_new in dirs_to_rename:
        try:
            if os.path.isdir(dir_path_old): # Check if source dir still exists
                os.rename(dir_path_old, dir_path_new)
                logging.debug(f"[RENAMED DIR] {dir_path_old} -> {dir_path_new}")
        except OSError as e:
            logging.debug(f"[ERROR] 디렉토리 이름 변경 실패: {dir_path_old} -> {dir_path_new}")
            logging.debug(e)
            traceback.print_exc()
