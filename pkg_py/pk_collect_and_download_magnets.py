import traceback

#  import collect_magnet_set, get_f_current_n, pk_deprecated_get_d_current_n_like_person

from colorama import init as pk_colorama_init

# from pkg_py.system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED
#

if __name__ == '__main__':
    try:

        ensure_colorama_initialized_once()

        collect_magnet_set()
        # load_magnet_set_to_bittorrent()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
        d_current_n = pk_deprecated_get_d_current_n_like_person()
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        traceback_format_exc_list = traceback.format_exc().split("\n")

        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            ensure_printed(str_working=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
