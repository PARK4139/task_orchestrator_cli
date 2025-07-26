from pkg_py.functions_split import test_pk_python_program_structure
from pkg_py.functions_split.debug_this_code_operated import ensure_this_code_operated
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_value_via_fzf_or_history_routine import get_value_via_fzf_or_history_routine
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.local_test_activate import LTA


def ensure_function_name_python_file_created():
    import inspect
    import logging
    import os

    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    from pkg_py.system_object.directories import D_PKG_PY, D_FUNCTIONS_SPLIT
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.system_object.files import F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY

    func_n = inspect.currentframe().f_code.co_name

    while True:
        # 1. 디렉토리 경로 입력 받기
        d_working = get_value_completed(
            key_hint='d_working=',
            values=[D_PKG_PY, D_FUNCTIONS_SPLIT]
        )
        if not os.path.isdir(d_working):
            logging.info(f"[{PkMessages2025.PATH_NOT_FOUND}] {d_working}")
            continue

        # 2. 파일명 입력 받기 (.py 확장자 자동 부여)
        key_name = 'python_file_name'
        func_n = inspect.currentframe().f_code.co_name
        file_id = get_file_id(key_name, func_n)
        editable = False
        # editable = True
        init_options = ["pk_ensure_", "ensure_"]
        value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
        f_n = value
        if not value.endswith(".py"):
            value += ".py"
        python_file_name = value
        ensure_printed(f'''python_file_name={python_file_name} {'%%%FOO%%%' if LTA else ''}''')


        counter = 1

        # 3. 중복 파일 처리
        while os.path.exists(os.path.join(d_working, python_file_name)):
            python_file_name = f_n.replace(".py", f"_DUPLICATED_{counter:03}.py")
            counter += 1

        # 중복 처리 끝난 후에 전체 경로 구성
        f_pnx_downloaded = os.path.join(d_working, python_file_name)

        # 4. 템플릿 옵션 선택
        template_option = get_value_completed(key_hint='template_file=', values=[F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY])
        F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY = get_pnx_os_style(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY)

        # 5. 파일 생성
        ensure_pnx_made(pnx=f_pnx_downloaded, mode="f")
        logging.info(f"[{PkMessages2025.CREATED}] {f_pnx_downloaded}")

        # 6. 템플릿 내용 복사
        # 템플릿 복사 처리: 파일 내용을 직접 읽어서 쓰기
        if template_option == F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY:
            if os.path.isfile(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY):
                try:
                    with open(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY, 'r', encoding='utf-8') as f_template:
                        template_content = f_template.read()
                        ensure_printed(f'''[{PkMessages2025.DATA}] template_content={template_content} {'%%%FOO%%%' if LTA else ''}''')

                    with open(f_pnx_downloaded, 'w', encoding='utf-8') as f_new:
                        f_new.write(template_content)

                    logging.info(f"[{PkMessages2025.COPIED}] content copied → {f_pnx_downloaded}")
                except Exception as e:
                    logging.info(f"[{PkMessages2025.FAILED}] write template: {e}")
            else:
                logging.info(f"[{PkMessages2025.SKIPPED}] template file not found: {F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY}")

        # 7. 생성된 파일 열기
        ensure_pnx_opened_by_ext(pnx=f_pnx_downloaded)


