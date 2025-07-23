import traceback

from colorama import init as pk_colorama_init

# from pkg_py.pk_system_object.500_live_logic import pk_kill_pk_program_list
# from pkg_py.pk_system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED
#

if __name__ == "__main__":
    try:

        pk_colorama_init_once()

        pk_kill_pk_program_list()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
