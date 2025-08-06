if __name__ == "__main__":
    import traceback

    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_process_killed_by_pid import ensure_process_killed_by_pid
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        # 파일명에서 함수명 추출
        import os

        file_name = os.path.basename(__file__)
        func_n = file_name.replace('.py', '')

        key_name = "pid"
        pid = get_values_from_historical_file_routine(
            file_id=get_file_id(key_name, func_n),
            key_hint=f'{key_name}=',
            options_default=[],
            editable=True
        )

        # PID를 정수로 변환
        try:
            pid = int(pid)
            ensure_process_killed_by_pid(pid=pid)
        except ValueError:
            print(f"❌ 유효하지 않은 PID입니다: {pid}")

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
        import traceback
