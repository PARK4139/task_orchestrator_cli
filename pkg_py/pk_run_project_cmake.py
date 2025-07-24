# -*- coding: utf-8 -*-





if __name__ == '__main__':
    try:

        import traceback

        #  import chcp_65001
        #  import is_os_windows, get_f_current_n, pk_deprecated_get_d_current_n_like_person
        #, D_PROJECT, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
        # from pkg_py.system_object.500_live_logic import assist_to_run_project_cmake
        #
        if is_os_windows():
            chcp_65001()
        assist_to_run_project_cmake()
        pk_print(str_working=assist_to_run_project_cmake.__name__)

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
        d_current_n = pk_deprecated_get_d_current_n_like_person()
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        traceback_format_exc_list = traceback.format_exc().split("\n")

        pk_print(str_working=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(str_working=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        pk_print(str_working=f'{PK_UNDERLINE}', print_color='red')

        pk_print(str_working=f'{PK_UNDERLINE}\n', print_color="yellow")
        pk_print(str_working=f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n}\nd_current={d_current_n}\n', print_color="yellow")
        pk_print(str_working=f'{PK_UNDERLINE}\n', print_color="yellow")

        
