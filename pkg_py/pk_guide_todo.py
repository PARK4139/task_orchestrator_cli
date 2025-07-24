if __name__ == "__main__":
    
    #  import get_d_current_n_like_person, get_f_current_n, guide_todo
    #

    try:
        
        #  import get_d_current_n_like_person, get_f_current_n, add_todo, guide_todo
        #

        guide_todo()

    except:
        f_current_n= get_f_current_n()
        d_current_n=get_d_current_n_like_person()
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        traceback_format_exc_list = traceback.format_exc().split("\n")
        
        pk_print(str_working=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            pk_print(str_working=f'{STAMP_EXCEPTION_OCCURED} {traceback_format_exc_str}', print_color='red')
        pk_print(str_working=f'{PK_UNDERLINE}', print_color='red')

        pk_print(str_working=f'{PK_UNDERLINE}\n', print_color="yellow")
        pk_print(str_working=f'{STAMP_PYTHON_DEBUGGING_NOTE} f_current={f_current_n}\nd_current={d_current_n}\n', print_color="yellow")
        pk_print(str_working=f'{PK_UNDERLINE}\n', print_color="yellow")

        