# -*- coding: utf-8 -*-
if __name__ == '__main__':
    try:
        #  import (
            pk_deprecated_get_d_current_n_like_person,
            get_f_current_n, chcp_65001, get_os_n,
            pk_ensure_f_list_organized_by_keyword_and_x
        )
        #, D_PROJECT
        #, print_yellow

        if get_os_n() == 'windows':
            chcp_65001()

        pk_ensure_f_list_organized_by_keyword_and_x()
    except Exception as e:
        import traceback

        ensure_printed(str_working=f'{PK_UNDERLINE}예외발생 s\n\n', print_color='red')
        ensure_printed(f'''{traceback.format_exc()} %%%FOO%%%''', print_color='red')
        ensure_printed(str_working=f'{PK_UNDERLINE}예외발생 e\n\n', print_color='red')

        ensure_printed(str_working=f'{PK_UNDERLINE}[Debugging Note] s\n', print_color="yellow")
        f_current = get_f_current_n()
        d_current = pk_deprecated_get_d_current_n_like_person()
        print_yellow(prompt=f'f_current={f_current}\nd_current={d_current}\n')
        ensure_printed(str_working=f'{PK_UNDERLINE}[Debugging Note] e\n', print_color="yellow")
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        ensure_printed(script_to_run_python_program_in_venv)
