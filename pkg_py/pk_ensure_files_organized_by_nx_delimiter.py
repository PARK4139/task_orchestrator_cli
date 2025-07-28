if __name__ == '__main__':
    try:
        import traceback

        pk_assist_to_ensure_files_organized_by_nx_delimiter()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
