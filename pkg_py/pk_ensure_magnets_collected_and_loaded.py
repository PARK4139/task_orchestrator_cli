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
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
