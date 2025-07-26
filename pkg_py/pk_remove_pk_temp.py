__author__ = 'pk == junghoon.park'

if __name__ == "__main__":
    try:
        from colorama import init as pk_colorama_init

        # from pkg_py.system_object.500_live_logic import copy, ensure_command_excuted_to_os, is_os_windows, kill_self_pk_program
        #, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        #

        colorama_init_once()

        if is_os_windows():
            ensure_command_excuted_to_os(cmd='echo y | rmdir /s %USERPROFILE%\Downloads\pk_working\pk_temp')

        kill_self_pk_program(self_f=__file__)

    except:
        import traceback

        traceback_format_exc_list = traceback.format_exc().split("\n")
        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            # ensure_printed(str_working=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
            ensure_printed(str_working=f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
