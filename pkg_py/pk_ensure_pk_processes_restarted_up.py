if __name__ == "__main__":
    try:
        import traceback

        # from pkg_py.system_object.500_live_logic import ensure_pk_processes_restarted_up, ensure_copied
        #
        # from pkg_py.system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED

        ensure_pk_processes_restarted_up()

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
