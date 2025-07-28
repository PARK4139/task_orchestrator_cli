if __name__ == "__main__":
    import traceback
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.functions_split.ensure_input_preprocessed import ensure_input_preprocessed
    from pkg_py.functions_split.ensure_os_shutdown_v2 import ensure_os_shutdown_v2
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    try:
        seconds = ensure_input_preprocessed(str_working=f"seconds=", upper_seconds_limit=10, return_default=f"{10}")
        seconds = seconds.strip()
        ensure_os_shutdown_v2(seconds)

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
