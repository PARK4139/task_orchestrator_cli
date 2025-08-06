if __name__ == '__main__':
    from pkg_py.functions_split.ensure_hotkey_monitor_started import ensure_hotkey_monitor_as_service
    from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started
    from pkg_py.functions_split.ensure_pk_system_started_ultra_fast import ensure_pk_system_started_ultra_fast
    import traceback
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once

    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config

    # cmd : setx PYTHONPATH %USERPROFILE%\Downloads\pk_system
    # cmd : .venv\Scripts\python.exe pkg_py\pk_ensure_pk_system_started.py

    # ensure_pk_system_exit_silent()  # pk_test

    try:
        initialize_and_customize_logging_config(__file__)

        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))
        # ensure_pk_system_started() # too slow            # 원인분석결과 시간성능저하 주원인 : venv 활성화 시간,  uv python 실행시간
        ensure_pk_system_started_ultra_fast()  # slow      # 원인분석결과 시간성능저하 주원인 : venv 활성화 시간,  uv python 실행시간

        # ensure_hotkey_monitor_as_service(__file__)       # 원인분석결과 시간성능저하 개선요소 : venv 활성화 시간(초기 1회로 제한),  uv python 실행시간(초기 1회로 제한)
        # todo       end -> minimize    and    move to front, monitor loop 에 ensure_slept 추가
        #  skim/fzy 으로 전환 성능비교테스트

        # ensure_program_suicided(__file__) # pk_option
    except:
        traceback.print_exc()
