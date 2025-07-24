if __name__ == "__main__":
    import traceback
    try:
        seconds = ensure_input_preprocessed(str_working=f"seconds=", upper_seconds_limit=10, return_default=f"{10}")
        seconds = seconds.strip()
        make_os_shutdown(seconds=seconds)

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
