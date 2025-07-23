def ensure_pnx_made(pnx, mode, script_list=None, mode_script_overwrite=0):
    from pkg_py.pk_system_object.local_test_activate import LTA
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    import traceback
    import inspect
    import os
    pnx = get_pnx_os_style(pnx=pnx)
    func_n = inspect.currentframe().f_code.co_name
    state_pnx_duplicated = 0
    if mode == "f":
        if not does_pnx_exist(pnx=pnx):
            try:
                os.makedirs(os.path.dirname(pnx))
            except:
                pass
            cmd_to_os(rf'chcp 65001 >nul')
            cmd_to_os(rf'echo. > "{pnx}"')
        if script_list:
            while 1:
                if does_pnx_exist(pnx):
                    state_pnx_duplicated = 1
                    break
                elif does_pnx_exist(pnx):
                    state_pnx_duplicated = 0
                    break
            if state_pnx_duplicated == 1:
                pk_print(f'''state_pnx_duplicated={state_pnx_duplicated} {'%%%FOO%%%' if LTA else ''}''')
                # cmd_to_os(f'code {pnx}')
            if os.path.exists(pnx):
                # write script to f
                mode_open = None
                if mode_script_overwrite == 1:
                    mode_open = 'w'
                elif mode_script_overwrite == 0:
                    mode_open = 'a'
                with open(file=pnx, mode=mode_open, newline='\r\n') as f_obj:  # CRLF 개행 설정
                    # with open(file=pnx, mode=mode_open, newline='\n') as f_obj:  # LF 개행
                    for line in script_list:
                        f_obj.write(f"{line}\n")
                        pk_print(f'''{line} written to {pnx} {'%%%FOO%%%' if LTA else ''}''')
                    std_list = cmd_to_os(f'type {pnx}')
                    # 마지막줄 쓰였는지 확인
                    last_line = script_list[-1].replace("\n", "")
                    if last_line == std_list[-1].replace("\n", ""):
                        pk_print(f'''{last_line} written to {pnx} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
                    else:
                        pk_print(f'''{last_line} written to {pnx} {'%%%FOO%%%' if LTA else ''}''', print_color='red')
                        raise
    elif mode == "d":
        if not os.path.exists(pnx):
            os.makedirs(pnx)
    else:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return
