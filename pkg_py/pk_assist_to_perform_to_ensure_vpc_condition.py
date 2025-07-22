# -*- coding: utf-8 -*-
if __name__ == '__main__':
    try:
        import traceback

        #  import chcp_65001, assist_to_perform_to_ensure_vpc_condition
        #  import is_os_windows
        # from pkg_py.pk_system_object.500_live_logic import pk_deprecated_get_d_current_n_like_person, get_f_current_n, pk_copy
        # from pkg_py.pk_system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED
        #

        if is_os_windows():
            chcp_65001()

        assist_to_perform_to_ensure_vpc_condition()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
