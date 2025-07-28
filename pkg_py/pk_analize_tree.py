# -*- coding: utf-8 -*-


pass

if __name__ == '__main__':
    try:
        # ___________________________________________________________________________
        if get_os_n() == 'windows':
            chcp_65001()

        while 1:
            analize_tree(d_src=rf"D:\pk_classifying")
            ensure_slept(hours=3)
        # ___________________________________________________________________________
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
