from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_value_via_fzf_or_history_routine import get_value_via_fzf_or_history_routine
from pkg_py.system_object.directories import D_SYSTEM_OBJECT
from pkg_py.system_object.local_test_activate import LTA


def write_template_to_file(f_template, template_content):
    with open(f_template, 'w', encoding='utf-8') as f_new:
        f_new.write(template_content)


def ensure_function_name_python_file_created():
    # TODO : pk 파일을 만드는 옵션 or 단일 함수생성 옵션 or ...판단로직추가
    # TODO : pk 파일 생성시   structure 의 __main__ 줄 제거, 한단계 들여쓰기
    import inspect
    import logging
    import os

    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    from pkg_py.system_object.directories import D_PKG_PY, D_PK_FUNCTIONS_SPLIT
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.system_object.files import F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY

    func_n = inspect.currentframe().f_code.co_name

    D_PKG_PY = get_pnx_os_style(D_PKG_PY)
    D_PK_FUNCTIONS_SPLIT = get_pnx_os_style(D_PK_FUNCTIONS_SPLIT)

    while True:
        # 1. 디렉토리 경로 입력 받기
        d_working = get_value_completed(            key_hint='d_working=',            values=[D_PKG_PY, D_PK_FUNCTIONS_SPLIT, D_SYSTEM_OBJECT]        )
        d_working = get_pnx_os_style(d_working)
        if not os.path.isdir(d_working):
            logging.info(f"[{PkMessages2025.PATH_NOT_FOUND}] {d_working}")
            continue

        # 2. 파일명 입력 받기 (.py 확장자 자동 부여)
        # editable = False
        editable = True
        key_name = None
        file_id = None
        init_options = None
        if d_working == D_PKG_PY:
            key_name = 'pk_python_file_name'
            file_id = get_file_id(key_name, func_n)
            init_options = ["pk_ensure_", ]
        elif d_working == D_PK_FUNCTIONS_SPLIT:
            # key_name = 'python_file_name'
            key_name = 'pk_python_file_name'
            file_id = get_file_id(key_name, func_n)
            # init_options = ["ensure_"]
            init_options = [""]
        elif d_working == D_SYSTEM_OBJECT:
            key_name = 'python_system_object_file_name'
            file_id = get_file_id(key_name, func_n)
            init_options = [""]
        value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
        f_n = value
        if not value.endswith(".py"):
            value += ".py"
        python_file_name = get_pnx_os_style(value)
        ensure_printed(f'''python_file_name={python_file_name} {'%%%FOO%%%' if LTA else ''}''')

        # 3. 중복 파일 처리
        counter = 1
        func_n_template = f_n[:-3] if f_n.endswith(".py") else f_n
        while os.path.exists(os.path.join(d_working, python_file_name)):
            python_file_name = f"{func_n_template}_DUPLICATED_{counter:03}.py"
            counter += 1
            logging.info(f"[LOOP] checking: {python_file_name}")

        # 중복 처리 끝난 후에 전체 경로 구성
        function_name_python_file_pnx = os.path.join(d_working, python_file_name)
        ensure_printed(f'''[{PkMessages2025.DATA}] function_name_python_file_pnx={function_name_python_file_pnx} {'%%%FOO%%%' if LTA else ''}''')

        # 4. 템플릿 옵션 선택
        template_option = None
        # template_option = get_value_completed(key_hint='template_file=', values=[F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY, splited_function_template])
        if d_working == D_PKG_PY:
            template_option = F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY
        elif d_working == D_PK_FUNCTIONS_SPLIT:
            pass
        elif d_working == D_SYSTEM_OBJECT:
            pass
        F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY = get_pnx_os_style(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY)
        ensure_printed(f'''[{PkMessages2025.DATA}] template_option={template_option} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''[{PkMessages2025.DATA}] F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY={F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY} {'%%%FOO%%%' if LTA else ''}''')

        # 5. 파일 생성
        ensure_pnx_made(pnx=function_name_python_file_pnx, mode="f")
        logging.info(f"[{PkMessages2025.CREATED}] {function_name_python_file_pnx}")

        # 6. 템플릿 내용 복사
        template_content = None
        if d_working == D_PKG_PY:
            if os.path.isfile(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY):
                try:
                    with open(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY, 'r', encoding='utf-8') as f_template:
                        template_content = f_template.read()
                        ensure_printed(f'''[{PkMessages2025.DATA}] template_content={template_content} {'%%%FOO%%%' if LTA else ''}''')
                    write_template_to_file(function_name_python_file_pnx, template_content)
                    logging.info(f"[{PkMessages2025.COPIED}] template copied → {function_name_python_file_pnx}")
                except Exception as e:
                    logging.info(f"[{PkMessages2025.FAILED}] write template: {e}")
            else:
                logging.info(f"[{PkMessages2025.SKIPPED}] template file not found: {F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY}")
        elif d_working == D_PK_FUNCTIONS_SPLIT:
            template_content = f"def {func_n_template}():\n\tpass"
            ensure_printed(f'''[{PkMessages2025.DATA}] template_content={template_content} {'%%%FOO%%%' if LTA else ''}''')
            write_template_to_file(function_name_python_file_pnx, template_content)
            logging.info(f"[{PkMessages2025.COPIED}] template copied → {function_name_python_file_pnx}")
        elif d_working == D_SYSTEM_OBJECT:
            template_content = f"class "
            ensure_printed(f'''[{PkMessages2025.DATA}] template_content={template_content} {'%%%FOO%%%' if LTA else ''}''')
            write_template_to_file(function_name_python_file_pnx, template_content)
            logging.info(f"[{PkMessages2025.COPIED}] template copied → {function_name_python_file_pnx}")

        # 7. 생성된 파일 열기
        ensure_pnx_opened_by_ext(pnx=function_name_python_file_pnx)
