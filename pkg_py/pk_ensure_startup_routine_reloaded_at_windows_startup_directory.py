if __name__ == '__main__':
    import traceback

    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_startup_routine_reloaded_at_windows_startup_directory import ensure_startup_routine_reloaded_at_windows_startup_directory
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config
    from pkg_py.system_object.map_massages import PkMessages2025

    try:
        # 로깅 설정 초기화
        initialize_and_customize_logging_config(__file__)
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        ensure_printed(f"[{PkMessages2025.STARTED}] 시작프로그램 관리 재등록(pk_System)", print_color="blue")
        ensure_printed(f" 시작프로그램 관리 재등록(pk_System)", print_color="blue")
        ensure_startup_routine_reloaded_at_windows_startup_directory()

        # ensure_command_excuted_to_os(cmd=rf"{D_HOME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\pk_system_startup.lnk")
        # ensure_process_and_window_deduplicated_all()


    except Exception as e:
        ensure_printed(f"❌ 오류가 발생했습니다: {str(e)}", print_color="red")
        traceback.print_exc()
