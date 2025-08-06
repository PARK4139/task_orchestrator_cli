if __name__ == '__main__':
    try:
        import traceback

        pk_assist_to_ensure_files_organized_by_nx_delimiter()

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
