from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_modules_imported_proper():
    import inspect
    import os
    from pkg_py.refactor.pk_ensure_modules_imported_proper import save_imports_to_txt, open_txt_file_for_editing, preview_lazy_import_applied_code, backup_f_working, announce_start_applying, confirm_editing_done

    from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    from pkg_py.system_object.directories import D_ARCHIVED, D_PKG_PY

    func_n = inspect.currentframe().f_code.co_name

    initialize_and_customize_logging_config(__file__=__file__)
    d_working = D_PKG_PY

    # 1단계: import 수집 및 저장
    f_txt = save_imports_to_txt(d_working=d_working, func_n=func_n)

    # 2단계: txt 자동 열기
    open_txt_file_for_editing(f_txt)

    # 3단계: 편집 완료 여부 확인
    if not confirm_editing_done():
        print("[INFO] 사용자가 편집을 완료하지 않아 작업을 종료합니다.")
        exit(0)

    # 4단계: 적용 시작 안내
    announce_start_applying()

    f_working = "TODO"  # pk_option
    d_backup_target = D_ARCHIVED
    backup_path = backup_f_working(f_working, d_backup_target)

    # 1. f_working 내용 읽기
    with open(f_working, encoding='utf-8') as f:
        original_code = f.read()

    # 2. lazy import 목록 읽기
    lazy_imports = open(f_txt, encoding='utf-8').read().splitlines()

    # 3. PREVIEW 코드 생성
    preview_code = preview_lazy_import_applied_code(original_code, lazy_imports)

    # 4. PREVIEW 저장 및 열기
    preview_path = f"{os.path.splitext(f_working)[0]}_preview.py"
    with open(preview_path, "w", encoding='utf-8') as f:
        f.write(preview_code)

    print(f"[STEP6]  PREVIEW 저장 완료: {preview_path}")
    ensure_pnx_opened_by_ext(preview_path)
