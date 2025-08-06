from pkg_py.functions_split.ensure_drag_changed_printed  import ensure_drag_changed_printed 




if __name__ == "__main__":
    try:
        ensure_drag_changed_printed ()

    except:
        f_current_n= get_f_current_n()
        d_current_n=get_d_current_n_like_person()
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
        traceback_format_exc_list = traceback.format_exc().split("\n")
        
        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            ensure_printed(str_working=f'{STAMP_EXCEPTION_OCCURED} {traceback_format_exc_str}', print_color='red')
        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')

        ensure_printed(str_working=f'{PK_UNDERLINE}\n', print_color="yellow")
        ensure_printed(str_working=f'{'[ DEBUGGING NOTE ]'} f_current={f_current_n}\nd_current={d_current_n}\n', print_color="yellow")
        ensure_printed(str_working=f'{PK_UNDERLINE}\n', print_color="yellow")

        

