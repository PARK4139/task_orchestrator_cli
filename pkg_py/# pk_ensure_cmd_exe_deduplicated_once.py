if __name__ == '__main__':
    try:
        from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
        from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
        from pkg_py.functions_split.ensure_cmd_exe_deduplicated_once import ensure_cmd_exe_deduplicated_once
        import traceback
        from pkg_py.system_object.directories_reuseable import D_PROJECT
        from pkg_py.system_object.etc import PK_UNDERLINE
        from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
        from pkg_py.functions_split.is_os_windows import is_os_windows
        from pkg_py.functions_split.ensure_printed import ensure_printed
        from pkg_py.functions_split.ensure_windows_deduplicated import ensure_windows_deduplicated
        from pkg_py.functions_split.chcp_65001 import chcp_65001
        from pkg_py.functions_split.get_f_current_n import get_f_current_n
        from pkg_py.functions_split.deprecated_get_d_current_n_like_person import deprecated_get_d_current_n_like_person

        # if is_os_windows():
        #     chcp_65001()
        ensure_cmd_exe_deduplicated_once()
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
