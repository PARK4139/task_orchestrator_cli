# -*- coding: utf-8 -*-


if __name__ == '__main__':
    try:
        import traceback

        # from pkg_py.pk_system_object.500_live_logic import pk_copy, assist_to_analize_addup_issue
        #
        # from pkg_py.pk_system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED

        assist_to_analize_addup_issue()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
