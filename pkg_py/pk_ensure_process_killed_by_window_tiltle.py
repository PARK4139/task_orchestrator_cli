from pkg_py.functions_split.get_list_calculated import get_list_calculated

if __name__ == "__main__":
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
    from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
    from pkg_py.functions_split.get_set_from_list import get_set_from_list
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.gui_util import get_windows_opened
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    import traceback
    try:
        ensure_colorama_initialized_once()

        windows_opened = get_windows_opened()
        windows_opened = get_list_calculated(origin_list=windows_opened, dedup=True)
        window_title = get_value_completed(key_hint='window_title=', values=windows_opened)
        ensure_process_killed(window_title=window_title)

        if not LTA:
            ensure_pk_program_suicided(self_f=__file__)
    except Exception as exception:
        ensure_do_exception_routine(exception=exception, traceback=traceback)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)


