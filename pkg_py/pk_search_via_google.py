from pkg_py.pk_system_object.etc import PK_UNDERLINE

if __name__ == "__main__":
    try:
        # todo
        while 1:
            should_i_search_to_google()
            print()
            print()
            print()
            print()

    except:
        f_current_n= get_f_current_n()
        d_current_n=get_d_current_n_like_person()
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        traceback_format_exc_list = traceback.format_exc().split("\n")
        
        pk_print(working_str=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(working_str=f'{STAMP_EXCEPTION_OCCURED} {traceback_format_exc_str}', print_color='red')
        pk_print(working_str=f'{PK_UNDERLINE}', print_color='red')

        pk_print(working_str=f'{PK_UNDERLINE}\n', print_color="yellow")
        pk_print(working_str=f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n}\nd_current={d_current_n}\n', print_color="yellow")
        pk_print(working_str=f'{PK_UNDERLINE}\n', print_color="yellow")

        




