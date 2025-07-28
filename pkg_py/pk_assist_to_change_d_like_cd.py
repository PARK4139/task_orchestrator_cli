try:
    # from pkg_py.system_object.500_live_logic import cd, assist_to_change_d
    import traceback
    # from pkg_py.system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
    # from pkg_py.system_object.500_live_logic import deprecated_get_d_current_n_like_person, get_f_current_n, ensure_copied
    #
    from colorama import init as pk_colorama_init

    ensure_colorama_initialized_once()

    assist_to_change_d()

except Exception as exception:
    ensure_do_exception_routine(traceback=traceback, exception=exception)
finally:
    ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)





