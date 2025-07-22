#!/usr/bin/env python   # shebang
# -*- coding: utf-8 -*- # encoding declaration
__author__ = 'pk == junghoon.park'


if __name__ == "__main__":
    try:
        import traceback

        from colorama import init as pk_colorama_init

        # from pkg_py.pk_system_object.500_live_logic import pk_copy, kill_self_pk_program, LTA, get_window_opened_list, pk_kill_process, get_value_completed, get_set_from_list
        #, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        #

        pk_colorama_init_once()

        window_opened_list = get_window_opened_list()
        window_opened_set = get_set_from_list(window_opened_list)
        window_title = get_value_completed(key_hint='window_title=', values=window_opened_set)
        pk_kill_process(window_title=window_title)

        if not LTA:
            kill_self_pk_program(self_f=__file__)
    except:
        # traceback_format_exc_list = traceback.format_exc().split("\n")
        # pk_print(working_str=f'{PK_UNDERLINE}', print_color='red')
        # for traceback_format_exc_str in traceback_format_exc_list:
        #     # pk_print(working_str=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        #     pk_print(working_str=f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        # pk_print(working_str=f'{PK_UNDERLINE}', print_color='red')
        # from pkg_py.pk_system_object.print_red import print_red

        traceback_format_exc_list = traceback.format_exc().split("\n")
        print_red(PK_UNDERLINE)
        for line in traceback_format_exc_list:
            print_red(f'{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line}')
        print_red(PK_UNDERLINE)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
