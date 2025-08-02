def ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str, target_extensions=None):
    import inspect
    import os

    from pkg_py.system_object.map_massages import PkMessages2025
    target_extensions = target_extensions or [".py", ".cmd", ".bat", ".ps1", ".sh"]
    func_n = inspect.currentframe().f_code.co_name
    d_target = os.path.abspath(d_target)

    if not os.path.isdir(d_target):
        print(f"[ERROR] 디렉토리 없음: {d_target}")
        return

    # ✨ 처리할 확장자 목록 (유지보수 편하게 리스트로)

    for root, dirs, files in os.walk(d_target):
        for filename in files:
            if not any(filename.lower().endswith(ext) for ext in target_extensions):
                continue  # 지정된 확장자 외 파일은 스킵

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
                # print(f"[SKIP] 변경 없음: {old_path}") # pk_option
                pass


