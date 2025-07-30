from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_pk_system_started_v3(file_list: list[str]):
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.run_pk_system_process_by_path import run_pk_system_process_by_path
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.print_pk_ls import print_pk_ls
    from pkg_py.functions_split.get_pk_system_process_pnxs import get_pk_system_process_pnxs
    from pkg_py.functions_split.guide_pk_error_mssage import guide_pk_error_mssage
    from pkg_py.functions_split.guide_to_use_pk_system_process import guide_to_use_pk_system_process
    from pkg_py.functions_split.print_pk_ver import print_pk_ver
    import sys
    try:

        if LTA:
            ensure_printed(f'''[{PkMessages2025.DATA}] len(sys.argv)={len(sys.argv)} {'%%%FOO%%%' if LTA else ''}''')
        if len(sys.argv) == 1:
            print_pk_ls(file_list)
            return

        arg1 = sys.argv[1]
        if arg1 in ['--version', '-v', 'ver']:
            ensure_printed(f"[{PkMessages2025.VERSION_INFO}]")
            print_pk_ver()
            return
        if arg1 in ['--list', '-l', 'ls']:
            ensure_printed(f"[{PkMessages2025.LISTED}]")
            print_pk_ls(file_list)
            return

        if arg1.isdigit():
            idx = int(arg1)
            if 0 <= idx < len(file_list):
                filepath = file_list[idx]
                if LTA:
                    ensure_printed(f"[{PkMessages2025.STARTED}] {filepath}")
                run_pk_system_process_by_path(filepath, sys.argv[2:])
                return
            else:
                ensure_printed(f"[{PkMessages2025.ERROR}] {PkMessages2025.ERROR_MASSAGE}")
                guide_pk_error_mssage()
                return
        else:
            guide_to_use_pk_system_process(get_pk_system_process_pnxs(), nx_by_user_input=arg1)
            return

    except Exception:
        import traceback
        traceback.print_exc()
