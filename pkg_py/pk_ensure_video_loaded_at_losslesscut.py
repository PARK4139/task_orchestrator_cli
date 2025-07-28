
if __name__ == "__main__":
    import traceback
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
    from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    try:

        ensure_colorama_initialized_once()

        ensure_video_loaded_at_losslesscut()

        if not LTA:
            ensure_pk_program_suicided(self_f=__file__)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
