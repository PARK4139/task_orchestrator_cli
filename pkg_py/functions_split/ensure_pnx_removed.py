def ensure_pnx_removed(pnx):
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.move_pnx_to_pk_recycle_bin import move_pnx_to_pk_recycle_bin
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.pk_system_object.local_test_activate import LTA

    import os
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    if not does_pnx_exist(pnx):
        pk_print(f'''삭제할 {get_nx(pnx)} 가 없습니다. {'%%%FOO%%%' if LTA else ''}''')
        return
    if does_pnx_exist(pnx):
        # 1
        # if is_f(pnx):
        #     cmd = rf'echo y | del /f "{pnx}"'
        # else:
        #     cmd = rf'echo y | rmdir /s "{pnx}"'
        # cmd_to_os(cmd=cmd)

        # 2
        # if does_pnx_exist(pnx):
        #     os.remove(pnx)

        # 3
        move_pnx_to_pk_recycle_bin(pnx)
    if not os.path.exists(pnx):
        pk_print(rf"[{func_n}] pnx={pnx} {'%%%FOO%%%' if LTA else ''}", print_color='green')
    else:
        pk_print(rf"[{func_n}] pnx={pnx} {'%%%FOO%%%' if LTA else ''}", print_color='red')
