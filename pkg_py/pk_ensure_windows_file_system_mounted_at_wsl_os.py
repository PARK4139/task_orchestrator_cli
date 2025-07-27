

import traceback

from colorama import init as pk_colorama_init

# from pkg_py.system_object.500_live_logic import ensure_tmux_pk_session_removed, get_nx, get_value_completed, get_pk_wsl_mount_d, get_pnxs, is_os_linux, ensure_slept, ensure_spoken
# from pkg_py.system_object.static_logic import D_PKG_PY, UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
#, print_red

colorama_init_once()

if __name__ == "__main__":
    try:

        # d_working = get_pnx_from_fzf()
        windows_path = get_value_completed(key_hint="windows_path=", values=[])
        # path_to_mount = get_value_completed(message="path_to_mount=", option_values=available_ip_without_localhost_list)
        d_pk_wsl_mount = get_pk_wsl_mount_d(windows_path=windows_path, path_to_mount='Downloads/pk_working')
        # d_pk_wsl_mount = get_pk_wsl_mount_d(windows_path=d_working, path_to_mount=path_to_mount)
        
        ensure_slept(100000)
        if is_os_linux():
            # ensure_command_excuted_to_os('exit')
            # available_pk_python_program_pnx = get_pnx_from_fzf(D_PKG_PY)
            available_pk_python_program_pnx = None
            pnx_list = get_pnxs(d_working=D_PKG_PY, mode="f", with_walking=0)
            for pnx in pnx_list:
                if __file__ not in pnx:
                    continue
                available_pk_python_program_pnx = pnx
            tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
            ensure_tmux_pk_session_removed(tmux_session)

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
