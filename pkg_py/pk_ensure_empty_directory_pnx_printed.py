
if __name__ == "__main__":
    from pkg_py.functions_split.ensure_empty_directory_pnx_printed import ensure_empty_directory_pnx_printed
    import traceback
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        root = D_PROJECT
        empty_dirs = ensure_empty_directory_pnx_printed(root)

        if empty_dirs:
            print("빈 디렉토리 목록:")
            for d in empty_dirs:
                print(f" - {d}")
        else:
            print("빈 디렉토리가 없습니다.")

        #     ensure_console_debuggable(ipdb) # pk_option
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)