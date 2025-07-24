
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    try:
        import traceback

        from colorama import init as pk_colorama_init

        #  import chcp_65001, is_os_windows
        # from pkg_py.system_object.500_live_logic import pk_assist_to_lock_os
        # from pkg_py.system_object.500_live_logic import pk_copy
        # from pkg_py.system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED
        #

        pk_colorama_init_once()

        if is_os_windows():
            chcp_65001()

        pk_assist_to_lock_os()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
