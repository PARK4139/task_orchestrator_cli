from pkg_py.functions_split.ensure_pk_system_process_reloaded_as_hot_reloader import ensure_pk_system_process_reloaded_as_hot_reloader

if __name__ == '__main__':
    import traceback
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE


    try:
        ensure_pk_system_process_reloaded_as_hot_reloader()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
