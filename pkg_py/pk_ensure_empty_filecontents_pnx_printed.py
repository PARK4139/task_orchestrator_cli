from pkg_py.functions_split.ensure_empty_filecontents_pnx_printed import ensure_empty_filecontents_pnx_printed

if __name__ == "__main__":
    import traceback
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))


        root = D_PROJECT
        empty_files = ensure_empty_filecontents_pnx_printed(
            root_dir=root,
            allowed_extensions=(".py", ".txt", ".md", ".json", ".csv")
        )

        if empty_files:
            print("실질적으로 내용이 없는 파일 목록:")
            for f in empty_files:
                print(f" - {f}")
        else:
            print("내용이 비어 있는 파일이 없습니다.")

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)