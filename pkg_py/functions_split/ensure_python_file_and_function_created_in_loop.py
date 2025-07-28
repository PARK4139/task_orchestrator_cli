from pkg_py.functions_split.ensure_slept import ensure_slept
from pkg_py.functions_split.get_f_historical import get_history_file
from pkg_py.functions_split.get_last_history import get_last_history
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_p import get_p
from pkg_py.functions_split.save_to_history import save_to_history
from pkg_py.system_object.directories import D_SYSTEM_OBJECT
from pkg_py.system_object.etc import pk_
from pkg_py.system_object.local_test_activate import LTA


def write_template_to_file(f_template, template_content):
    with open(f_template, 'w', encoding='utf-8') as f_new:
        f_new.write(template_content)


def ensure_python_file_and_function_created(d_working, func_n):
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
    from pkg_py.system_object.files import F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY

    D_PKG_PY = get_pnx_os_style(D_PKG_PY)
    D_PK_FUNCTIONS_SPLIT = get_pnx_os_style(D_PK_FUNCTIONS_SPLIT)
    D_SYSTEM_OBJECT = get_pnx_os_style(D_SYSTEM_OBJECT)
    d_working = get_pnx_os_style(d_working)

    # 1. get user directory path
    # d_working = get_value_completed(key_hint='d_working=', values=[D_PKG_PY, D_PK_FUNCTIONS_SPLIT, D_SYSTEM_OBJECT])
    if not os.path.isdir(d_working):
        logging.info(f"[{PkMessages2025.PATH_NOT_FOUND}] {d_working}")

    # 2. get user filename  # .py 확장자 자동 부여
    # editable = False
    editable = True
    value = None
    if d_working == D_PKG_PY:
        key_name = 'pk_python_file_name'
        file_id = get_file_id(key_name, func_n)
        init_options = ["ensure_" ]
        if LTA:
            # value = "pk_deprecated"
            value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
        else:
            value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
        save_to_history(value, history_file=get_history_file(file_id=file_id))
    elif d_working == D_PK_FUNCTIONS_SPLIT:
        key_name = 'pk_python_file_name'
        file_id = get_file_id(key_name, func_n)
        init_options = ["ensure_" ]
        if LTA:
            # value = "pk_deprecated"
            # value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
            value = get_last_history(history_file=get_history_file(file_id=file_id))
        else:
            value = get_last_history(history_file=get_history_file(file_id=file_id))

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
    F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY = get_pnx_os_style(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY)

    # 4. select template_option
    template_option = None
    # template_option = get_value_completed(key_hint='template_file=', values=[F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY, splited_function_template])
    if d_working == D_PKG_PY:
        file_pnx_to_made = rf"{get_p(file_pnx_to_made)}/{pk_}{get_nx(file_pnx_to_made)}"
        file_pnx_to_made = get_pnx_os_style(file_pnx_to_made)
        template_option = F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY
    elif d_working == D_PK_FUNCTIONS_SPLIT:
        pass
    elif d_working == D_SYSTEM_OBJECT:
        pass
    ensure_printed(f'''[{PkMessages2025.DATA}] template_option={template_option} {'%%%FOO%%%' if LTA else ''}''')
    ensure_printed(f'''[{PkMessages2025.DATA}] F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY={F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY} {'%%%FOO%%%' if LTA else ''}''')

    # 5. make file
    ensure_pnx_made(pnx=file_pnx_to_made, mode="f")
    logging.info(f"[{PkMessages2025.CREATED}] {file_pnx_to_made}")

    # 6. select and save template_content
    template_content = None
    if d_working == D_PKG_PY:
        if os.path.isfile(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY):
            try:
                with open(F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY, 'r', encoding='utf-8') as f_template:
                    template_content = f_template.read()
                    lines = template_content.splitlines()
                    lines = lines[1:]
                    lines = [line for line in lines if "__main__" not in line] # 2. "__main__" 포함된 줄 제거
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
            logging.info(f"[{PkMessages2025.SKIPPED}] template file not found: {F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY}")
    elif d_working == D_PK_FUNCTIONS_SPLIT:
        template_content = f"def {func_n_template}():\n\tpass"
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

    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.system_object.directories import D_PKG_PY, D_PK_FUNCTIONS_SPLIT

    func_n = inspect.currentframe().f_code.co_name

    D_PKG_PY = get_pnx_os_style(D_PKG_PY)
    D_PK_FUNCTIONS_SPLIT = get_pnx_os_style(D_PK_FUNCTIONS_SPLIT)

    while True:
        # 1. get user directory path
        if LTA:
            # mode = "PK_FILE_AND_FUNCTIONS" # pk_option
            mode = get_value_completed(key_hint='mode=', values=["PK_FILE_AND_FUNCTIONS", "SYSTEM_OBJECT"])
        else:
            mode = get_value_completed(key_hint='mode=', values=["PK_FILE_AND_FUNCTIONS", "SYSTEM_OBJECT"])
        mode = get_pnx_os_style(mode)
        if mode == "PK_FILE_AND_FUNCTIONS":
            for d_working in [D_PKG_PY, D_PK_FUNCTIONS_SPLIT]:
                ensure_python_file_and_function_created(d_working, func_n)
                ensure_slept(milliseconds=100)
        if mode == "SYSTEM_OBJECT":
            d_working = D_SYSTEM_OBJECT
            ensure_python_file_and_function_created(d_working, func_n)
        ensure_slept(milliseconds=100)

        if LTA:
            break
