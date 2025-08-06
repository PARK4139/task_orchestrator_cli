if __name__ == "__main__":
    from pkg_py.functions_split.ensure_emojis_removed_from_functions_split import ensure_emojis_removed_from_functions_split
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.system_object.directories import D_PROJECT
    import traceback

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))
        
        ensure_printed("functions_split 폴더에서 이모지 제거 작업을 시작합니다...", print_color='green')
        
        # 실제 이모지 제거 함수 호출
        ensure_emojis_removed_from_functions_split()
        
        ensure_printed("이모지 제거 작업이 완료되었습니다.", print_color='blue')
        
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)