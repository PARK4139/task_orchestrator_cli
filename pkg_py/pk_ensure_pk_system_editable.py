from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.pk_ensure_memo_opened import pk_ensure_memo_opened

if __name__ == "__main__":
    from pkg_py.workspace.pk_workspace import is_a2z_office
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    import traceback

    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.system_object.files import F_PYCHARM64_EDITION_2024_02_04_EXE, F_PYCHARM64_EDITION_2025_01_03_EXE

    try:
        pk_colorama_init_once()

        pk_ensure_memo_opened()

        if is_a2z_office():
            f_pycharm = get_pnx_os_style(F_PYCHARM64_EDITION_2024_02_04_EXE)
        else:
            f_pycharm = get_pnx_os_style(F_PYCHARM64_EDITION_2025_01_03_EXE)
        cmd_to_os(cmd=f'"{f_pycharm}" "{D_PROJECT}"')

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
