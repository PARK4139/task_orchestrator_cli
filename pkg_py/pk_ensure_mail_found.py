from pkg_py.functions_split.ensure_mail_found import ensure_mail_found

if __name__ == "__main__":
    import traceback

    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
    from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        # write code here
        # state =
        ensure_mail_found()
        ensure_program_suicided(__file__) # pk_option
        # if state["state"]:
        #     ensure_program_suicided(__file__) # pk_option

        # if LTA:
        #     ensure_console_debuggable(ipdb)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
