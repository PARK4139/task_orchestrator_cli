def write_template_to_file(f_template, template_content):
    with open(f_template, 'w', encoding='utf-8') as f_new:
        f_new.write(template_content)


def ensure_function_only_created(func_n):
    """함수만 생성하는 로직 (functions_split 디렉터리에 ensure_ 파일 생성)"""
    from pkg_py.functions_split.get_f_historical import ensure_history_file_pnx_got
    from pkg_py.functions_split.save_to_history import save_to_history
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_value_via_fzf_or_history_routine import get_value_via_fzf_or_history_routine
    from pkg_py.functions_split.ensure_copied import ensure_copied
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    from pkg_py.system_object.directories import D_PK_FUNCTIONS_SPLIT
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025

    import logging
    import os

    # functions_split 디렉토리 설정
    d_working = get_pnx_os_style(D_PK_FUNCTIONS_SPLIT)

    # 1. 함수명 입력 (매번 사용자가 직접 선택하도록 변경)
    key_name_func = 'function_name_only'
    file_id_func = get_file_id(key_name_func, func_n)
    init_options_func = ["ensure_", "get_", "set_", "is_", "has_", "can_"]

    editable = False  # pk_option

    # 함수명도 매번 사용자가 직접 입력하도록 수정 (get_last_history 제거)
    function_name = get_value_via_fzf_or_history_routine(
        key_name=key_name_func,
        file_id=file_id_func,
        init_options=init_options_func,
        editable=editable
    )

    # 함수명 확인을 위한 디버깅 출력
    ensure_printed(f'''[DEBUG] 입력받은 함수명: "{function_name}" {'%%%FOO%%%' if LTA else ''}''', print_color='yellow')
    ensure_printed(f'''[DEBUG] 함수명 타입: {type(function_name)} {'%%%FOO%%%' if LTA else ''}''', print_color='yellow')

    # 함수명 정리 (공백, 개행 제거)
    function_name = function_name.strip() if function_name else ""
    ensure_printed(f'''[DEBUG] 정리된 함수명: "{function_name}" {'%%%FOO%%%' if LTA else ''}''', print_color='yellow')

    # 함수명 히스토리 저장
    save_to_history(function_name, history_file=ensure_history_file_pnx_got(file_id=file_id_func))

    # 2. 파일명 입력 (매번 사용자가 직접 선택하도록 - 히스토리 자동 적용 안함)
    key_name_file = 'pk_python_file_name_function_only'  # 별도 키 사용
    file_id_file = get_file_id(key_name_file, func_n)
    init_options_file = ["ensure_"]

    # 파일명은 항상 사용자가 직접 입력하도록 (get_last_history 사용 안함)
    file_base_name = get_value_via_fzf_or_history_routine(
        key_name=key_name_file,
        file_id=file_id_file,
        init_options=init_options_file,
        editable=editable
    )

    # 파일명 정리
    file_base_name = file_base_name.strip() if file_base_name else ""
    ensure_printed(f'''[DEBUG] 입력받은 파일명: "{file_base_name}" {'%%%FOO%%%' if LTA else ''}''', print_color='yellow')

    # 파일명 히스토리 저장
    save_to_history(file_base_name, history_file=ensure_history_file_pnx_got(file_id=file_id_file))

    # 파일명 처리 (.py 확장자 추가)
    extension = ".py"
    if not file_base_name.endswith(extension):
        file_name = f"{file_base_name}{extension}"
    else:
        file_name = file_base_name

    ensure_printed(f'''[{PkMessages2025.DATA}] function_name="{function_name}" {'%%%FOO%%%' if LTA else ''}''', print_color='cyan')
    ensure_printed(f'''[{PkMessages2025.DATA}] file_name="{file_name}" {'%%%FOO%%%' if LTA else ''}''', print_color='cyan')

    # 중복 파일 처리
    counter = 1
    original_file_name = file_name
    while os.path.exists(os.path.join(d_working, file_name)):
        base_name = original_file_name[:-3] if original_file_name.endswith(extension) else original_file_name
        file_name = f"{base_name}_DUPLICATED_{counter:03}.py"
        counter += 1
        logging.info(f"[LOOP] checking: {file_name}")

    # 전체 파일 경로
    file_pnx_to_made = os.path.join(d_working, file_name)
    ensure_printed(f'''[{PkMessages2025.DATA}] file_pnx_to_made={file_pnx_to_made} {'%%%FOO%%%' if LTA else ''}''')

    # 파일 생성
    ensure_pnx_made(pnx=file_pnx_to_made, mode="f")
    logging.info(f"[{PkMessages2025.CREATED}] {file_pnx_to_made}")

    # 함수 템플릿 생성 (함수명이 제대로 반영되는지 확인)
    template_content = f"""from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def {function_name}():
    \"\"\"
    {function_name} 함수의 설명을 여기에 작성하세요.
    \"\"\"
    pass
"""

    # 템플릿 내용 확인을 위한 디버깅 출력
    ensure_printed(f'''[DEBUG] 생성된 템플릿 내용:''', print_color='yellow')
    ensure_printed(template_content, print_color='white')

    # 파일에 템플릿 작성
    write_template_to_file(file_pnx_to_made, template_content)
    logging.info(f"[{PkMessages2025.COPIED}] template copied → {file_pnx_to_made}")

    ensure_printed(f'''[{PkMessages2025.SUCCESS}] Function file created!''', print_color='green')
    ensure_printed(f'''[{PkMessages2025.DATA}] Function name: {function_name}''', print_color='cyan')
    ensure_printed(f'''[{PkMessages2025.DATA}] File name: {file_name}''', print_color='cyan')
    ensure_printed(f'''[{PkMessages2025.DATA}] File path: {file_pnx_to_made}''', print_color='yellow')

    # 클립보드에 함수명 복사 (파일 작업 후 함수명만)
    ensure_copied(function_name)
    ensure_printed(f'''[{PkMessages2025.SUCCESS}] Function name copied to clipboard!''', print_color='green')

    # 생성된 파일 열기
    ensure_pnx_opened_by_ext(pnx=file_pnx_to_made)

    return file_pnx_to_made, function_name


def ensure_python_file_and_function_created(d_working, func_n):
    from pkg_py.functions_split.get_f_historical import ensure_history_file_pnx_got
    from pkg_py.functions_split.get_last_history import get_last_history
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_p import get_p
    from pkg_py.functions_split.save_to_history import save_to_history
    from pkg_py.system_object.etc import pk_

    import logging
    import os
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_value_via_fzf_or_history_routine import get_value_via_fzf_or_history_routine
    from pkg_py.system_object.directories import D_SYSTEM_OBJECT
    from pkg_py.system_object.local_test_activate import LTA

    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    from pkg_py.system_object.directories import D_PKG_PY, D_PK_FUNCTIONS_SPLIT
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.system_object.files import F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY

    D_PKG_PY = get_pnx_os_style(D_PKG_PY)
    D_PK_FUNCTIONS_SPLIT = get_pnx_os_style(D_PK_FUNCTIONS_SPLIT)
    D_SYSTEM_OBJECT = get_pnx_os_style(D_SYSTEM_OBJECT)
    d_working = get_pnx_os_style(d_working)

    # d_working = get_value_completed(key_hint='d_working=', values=[D_PKG_PY, D_PK_FUNCTIONS_SPLIT, D_SYSTEM_OBJECT])
    if not os.path.isdir(d_working):
        logging.info(f"[{PkMessages2025.PATH_NOT_FOUND}] {d_working}")

    editable = False
    # editable = True
    value = None
    if d_working == D_PKG_PY:
        key_name = 'pk_python_file_name'
        file_id = get_file_id(key_name, func_n)
        init_options = ["ensure_"]
        if LTA:
            # value = "pk_deprecated"
            value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
        else:
            value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
        save_to_history(value, history_file=ensure_history_file_pnx_got(file_id=file_id))
    elif d_working == D_PK_FUNCTIONS_SPLIT:
        key_name = 'pk_python_file_name'
        file_id = get_file_id(key_name, func_n)
        init_options = ["ensure_"]
        if LTA:
            # value = "pk_deprecated"
            # value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
            value = get_last_history(history_file=ensure_history_file_pnx_got(file_id=file_id))
        else:
            value = get_last_history(history_file=ensure_history_file_pnx_got(file_id=file_id))

    elif d_working == D_SYSTEM_OBJECT:
        key_name = 'python_system_object_file_name'
        file_id = get_file_id(key_name, func_n)
        init_options = []
        if LTA:
            value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
            # value = "pk_deprecated"
        else:
            value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
    f_n = value

    extension = ".py"  # pk_option
    if not value.endswith(extension):
        value += extension
    file_name = get_pnx_os_style(value)
    ensure_printed(f'''file_name={file_name} {'%%%FOO%%%' if LTA else ''}''')

    # 3. deduplicate files
    counter = 1
    func_n_template = f_n[:-3] if f_n.endswith(extension) else f_n
    while os.path.exists(os.path.join(d_working, file_name)):
        file_name = f"{func_n_template}_DUPLICATED_{counter:03}.py"
        counter += 1
        logging.info(f"[LOOP] checking: {file_name}")

    # 중복 처리 끝난 후에 전체 경로 구성
    file_pnx_to_made = os.path.join(d_working, file_name)
    ensure_printed(f'''[{PkMessages2025.DATA}] file_pnx_to_made={file_pnx_to_made} {'%%%FOO%%%' if LTA else ''}''')
    F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY = get_pnx_os_style(F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY)

    # 4. select template_option
    template_option = None
    # template_option = get_value_completed(key_hint='template_file=', values=[F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY, splited_function_template])
    if d_working == D_PKG_PY:
        file_pnx_to_made = rf"{get_p(file_pnx_to_made)}/{pk_}{get_nx(file_pnx_to_made)}"
        file_pnx_to_made = get_pnx_os_style(file_pnx_to_made)
        template_option = F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY
    elif d_working == D_PK_FUNCTIONS_SPLIT:
        pass
    elif d_working == D_SYSTEM_OBJECT:
        pass
    ensure_printed(f'''[{PkMessages2025.DATA}] template_option={template_option} {'%%%FOO%%%' if LTA else ''}''')
    ensure_printed(f'''[{PkMessages2025.DATA}] F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY={F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY} {'%%%FOO%%%' if LTA else ''}''')

    # 5. make file
    ensure_pnx_made(pnx=file_pnx_to_made, mode="f")
    logging.info(f"[{PkMessages2025.CREATED}] {file_pnx_to_made}")

    # 6. select and save template_content
    template_content = None
    if d_working == D_PKG_PY:
        if os.path.isfile(F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY):
            try:
                with open(F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY, 'r', encoding='utf-8') as f_template:
                    template_content = f_template.read()
                    lines = template_content.splitlines()
                    lines = lines[1:]

                    # lines = [line for line in lines if "__main__" not in line] #  "__main__" 포함된 줄 제거  # pk_option
                    def remove_one_indent(line):
                        if line.startswith('\t'):
                            return line[1:]
                        elif line.startswith('    '):  # 공백 4칸
                            return line[4:]
                        else:
                            return line

                    lines = [remove_one_indent(line) for line in lines]
                    template_content = "\n".join(lines)
                    ensure_printed(f'''[{PkMessages2025.DATA}] template_content={template_content} {'%%%FOO%%%' if LTA else ''}''')
                write_template_to_file(file_pnx_to_made, template_content)
                logging.info(f"[{PkMessages2025.COPIED}] template copied → {file_pnx_to_made}")
            except Exception as e:
                logging.info(f"[{PkMessages2025.FAILED}] write template: {e}")
        else:
            logging.info(f"[{PkMessages2025.SKIPPED}] template file not found: {F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY}")
    elif d_working == D_PK_FUNCTIONS_SPLIT:
        template_content = (f""
                            f"from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured\n"
                            f"@ensure_seconds_measured\n"
                            f"def {func_n_template}():\n"
                            f"\tpass"
                            f"")
        ensure_printed(f'''[{PkMessages2025.DATA}] template_content={template_content} {'%%%FOO%%%' if LTA else ''}''')
        write_template_to_file(file_pnx_to_made, template_content)
        logging.info(f"[{PkMessages2025.COPIED}] template copied → {file_pnx_to_made}")
    elif d_working == D_SYSTEM_OBJECT:
        template_content = f"class "
        ensure_printed(f'''[{PkMessages2025.DATA}] template_content={template_content} {'%%%FOO%%%' if LTA else ''}''')
        write_template_to_file(file_pnx_to_made, template_content)
        logging.info(f"[{PkMessages2025.COPIED}] template copied → {file_pnx_to_made}")

    # 7. open file generated
    ensure_pnx_opened_by_ext(pnx=file_pnx_to_made)


def ensure_python_file_and_function_created_in_loop():
    import inspect
    from pkg_py.functions_split.ensure_slept import ensure_slept
    from pkg_py.system_object.directories import D_SYSTEM_OBJECT
    from pkg_py.system_object.local_test_activate import LTA

    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.system_object.directories import D_PKG_PY, D_PK_FUNCTIONS_SPLIT

    func_n = inspect.currentframe().f_code.co_name

    D_PKG_PY = get_pnx_os_style(D_PKG_PY)
    D_PK_FUNCTIONS_SPLIT = get_pnx_os_style(D_PK_FUNCTIONS_SPLIT)

    while True:
        if LTA:
            # mode = "PK_FILE_AND_FUNCTIONS" # pk_option
            mode = get_value_completed(key_hint='mode=', values=[
                "PK_FILE_AND_FUNCTIONS",
                "SYSTEM_OBJECT",
                "FUNCTION_ONLY"  # 새로운 옵션 추가
            ])
        else:
            mode = get_value_completed(key_hint='mode=', values=[
                "PK_FILE_AND_FUNCTIONS",
                "SYSTEM_OBJECT",
                "FUNCTION_ONLY"  # 새로운 옵션 추가
            ])

        mode = get_pnx_os_style(mode)

        if mode == "PK_FILE_AND_FUNCTIONS":
            for d_working in [D_PKG_PY, D_PK_FUNCTIONS_SPLIT]:
                ensure_python_file_and_function_created(d_working, func_n)
                ensure_slept(milliseconds=100)
        elif mode == "SYSTEM_OBJECT":
            d_working = D_SYSTEM_OBJECT
            ensure_python_file_and_function_created(d_working, func_n)
        elif mode == "FUNCTION_ONLY":  # 새로운 모드 처리
            ensure_function_only_created(func_n)

        ensure_slept(milliseconds=100)

        if LTA:
            break
