__author__ = 'pk == junghoon.park'

if __name__ == "__main__":
    try:

        import traceback

        from colorama import init as pk_colorama_init

        # from pkg_py.system_object.500_live_logic import copy, cmd_to_os, is_os_windows, kill_self_pk_program, LTA
        #, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        #

        colorama_init_once()

        if is_os_windows():
            cmd_to_os(cmd='mkdir %USERPROFILE%\Downloads\pk_working\pk_temp')

        if not LTA:
            kill_self_pk_program(self_f=__file__)

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
