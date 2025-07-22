import traceback

from colorama import init as pk_colorama_init

#, print_red
# from pkg_py.pk_system_object.500_live_logic import cmd_to_os, pk_sleep
# from pkg_py.pk_system_object.static_logic import D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, UNDERLINE, STAMP_TRY_GUIDE, D_PROJECT_PARENTS


if __name__ == "__main__":
    try:
        pk_colorama_init_once()
        f_bat = f'call "{D_PROJECT_PARENTS}\pk_system\pk_push_project_to_github.bat"'
        std_list = cmd_to_os(f_bat)

        f_bat = f'call "{D_PROJECT_PARENTS}\pk_memo\pk_push_project_to_github.bat"'
        std_list = cmd_to_os(f_bat)

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
