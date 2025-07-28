def ensure_pycharm_opened():
    file_exe = get_pnx_os_style(F_PYCHARM64_EDITION_EXE)
    ensure_command_excuted_to_os(cmd=f'start "" "{file_exe}" "{D_PROJECT}"', mode="a")


def ensure_cursor_opened():
    file_exe = get_pnx_os_style(F_CURSOR_EXE)
    ensure_command_excuted_to_os(cmd=f'start "" "{file_exe}" "{D_PROJECT}"', mode="a")


if __name__ == "__main__":
    from pkg_py.functions_split.ensure_memo_editable import ensure_memo_editable
    from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    import traceback

    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.system_object.files import F_PYCHARM64_EDITION_EXE, F_PYCHARM64_EDITION_EXE, F_CURSOR_EXE

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        ensure_memo_editable()
        ensure_pycharm_opened()
        ensure_cursor_opened()

        ensure_process_killed(window_title=get_nx(__file__))  # pk_option

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
