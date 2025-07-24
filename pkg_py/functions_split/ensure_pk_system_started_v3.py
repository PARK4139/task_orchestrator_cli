from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds


@pk_measure_seconds
def ensure_pk_system_started_v3(file_list: list[str]):
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.run_pk_python_program_by_path import run_pk_python_program_by_path
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.print_pk_ls import print_pk_ls
    from pkg_py.functions_split.get_pk_system_process_pnx_list import get_pk_system_process_pnx_list
    from pkg_py.functions_split.guide_pk_error_mssage import guide_pk_error_mssage
    from pkg_py.functions_split.guide_to_use_pk_system_process import guide_to_use_pk_system_process
    from pkg_py.functions_split.print_pk_ver import print_pk_ver
    import sys
    try:

        if LTA:
            pk_print(f'''[{PkMessages2025.DATA}] len(sys.argv)={len(sys.argv)} {'%%%FOO%%%' if LTA else ''}''')
        if len(sys.argv) == 1:
            print_pk_ls(file_list)
            return

        arg1 = sys.argv[1]
        if arg1 in ['--version', '-v', 'ver']:
            pk_print(f"[{PkMessages2025.VERSION_INFO}]")
            print_pk_ver()
            return
        if arg1 in ['--list', '-l', 'ls']:
            pk_print(f"[{PkMessages2025.LISTED}]")
            print_pk_ls(file_list)
            return

        if arg1.isdigit():
            idx = int(arg1)
            if 0 <= idx < len(file_list):
                filepath = file_list[idx]
                if LTA:
                    pk_print(f"[{PkMessages2025.STARTED}] {filepath}")
                run_pk_python_program_by_path(filepath, sys.argv[2:])
                return
            else:
                pk_print(f"[{PkMessages2025.ERROR}] {PkMessages2025.ERROR_MASSAGE}")
                guide_pk_error_mssage()
                return
        else:
            guide_to_use_pk_system_process(get_pk_system_process_pnx_list(), nx_by_user_input=arg1)
            return

    except Exception:
        import traceback
        traceback.print_exc()
