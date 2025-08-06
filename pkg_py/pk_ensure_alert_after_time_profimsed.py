if __name__ == "__main__":
    from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
    import traceback
    from pkg_py.functions_split.ensure_alert_after_time_profimsed import ensure_alert_after_time_profimsed, get_time_input
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        # 사용자 입력 받기
        alarm_content, seconds, unit = get_time_input()
        
        if alarm_content is None:
            print("❌ 알람 설정을 취소합니다.")
        else:
            # 인자로 전달하여 함수 호출
            ensure_alert_after_time_profimsed(alarm_content, seconds, unit)

        ensure_program_suicided(__file__)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
