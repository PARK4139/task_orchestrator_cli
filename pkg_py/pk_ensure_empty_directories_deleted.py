if __name__ == "__main__":

    try:
        ensure_colorama_initialized_once()

        ensure_empty_directories_deleted()
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
