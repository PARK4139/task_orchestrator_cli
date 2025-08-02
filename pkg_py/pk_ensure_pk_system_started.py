if __name__ == '__main__':
    from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config
    import traceback
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_pk_system_started import ensure_pk_system_started

    try:
        # 로깅 설정 초기화 (프로젝트 기본 규칙: D_PKG_LOG에 저장)
        initialize_and_customize_logging_config(__file__)
        
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        # loop_mode = True # pk_option
        loop_mode = False  # pk_option

        if loop_mode == True:
            while True:
                ensure_pk_system_started()
        else:
            ensure_pk_system_started()

        # ensure_program_suicided(__file__) # pk_option
    except:
        traceback.print_exc()
