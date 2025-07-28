from pkg_py.functions_split.ensure_kiri_ran import ensure_kiri_ran

if __name__ == "__main__":
    try:
        import traceback

        #  import ensure_kiri_ran
        from pkg_py.functions_split.ensure_printed import ensure_printed

        # , D_PROJECT
        # from pkg_py.system_object.500_live_logic import copy
        # from pkg_py.system_object.static_logic import STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED

        ensure_kiri_ran()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
