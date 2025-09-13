import traceback

from functions import ensure_seconds_measured


def ensure_filename_and_file_content_text_replaced_core(f_target, old_text, new_text):
    from functions.get_p import get_p
    import os

    from functions.get_nx import get_nx

    modified = False

    # 파일 내용 수정
    try:
        with open(f_target, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"[SKIP] 바이너리 파일로 판단: {f_target}")
        return
    if old_text in content:
        new_content = content.replace(old_text, new_text)
        with open(f_target, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[MODIFIED CONTENT] {f_target}")
        modified = True

    # 파일명 변경
    filename = get_nx(f_target)
    root = get_p(f_target)
    if old_text in filename:
        new_filename = filename.replace(old_text, new_text)
        new_path = os.path.join(root, new_filename)
        if os.path.exists(new_path):
            print(f"[SKIP RENAME] Target already exists: {new_path}")
        else:
            try:
                os.rename(f_target, new_path)
                print(f"[RENAMED FILE] {f_target} → {new_path}")
            except FileExistsError:
                print(f"[ERROR] FileExistsError despite pre-check: {new_path}")
                traceback.print_exc()
        modified = True

    if not modified:
        # print(f"[SKIP] 변경 없음: {file_path_old}") # pk_option
        pass


def ensure_filename_and_file_content_text_replaced(d_target, old_text, new_text, target_extensions, ignored_directory_names):
    from pathlib import Path
    import os
    from sources.objects.pk_local_test_activate import LTA

    d_target = os.path.abspath(d_target)
    d_target = Path(d_target)
    d_target = str(d_target)
    print(f'''d_target={d_target} {'%%%FOO%%%' if LTA else ''}''')

    if not os.path.isdir(d_target):
        print(f"[ERROR] 디렉토리 없음: {d_target}")
        return

    for root, dirs, files in os.walk(d_target):
        for filename in files:
            if not any(filename.lower().endswith(ext) for ext in target_extensions):
                continue
            file_path_old = os.path.join(root, filename)
            ignored_detected = False
            for ignored_directory_name in ignored_directory_names:
                if ignored_directory_name in file_path_old:
                    ignored_detected = True
                    print(f"[SKIP] ignored_directory_names 중 {ignored_directory_name} 감지 in {file_path_old}")
                    continue
            if ignored_detected == True:
                continue
            ensure_filename_and_file_content_text_replaced_core(f_target=file_path_old, old_text=old_text, new_text=new_text)
