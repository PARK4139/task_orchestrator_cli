def ensure_routine_file_executed_as_hot_reloader():
    import inspect
    import logging
    import traceback
    from pathlib import Path
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SOURCES
    from sources.functions import ensure_spoken
    from sources.functions.ensure_chcp_65001 import ensure_chcp_65001
    from sources.functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
    from sources.functions.ensure_files_modified_time_stable import ensure_files_modified_time_stable
    from sources.functions.ensure_task_orchestrator_cli_useless_log_removed import ensure_task_orchestrator_cli_useless_log_removed
    from sources.functions.ensure_process_killed import ensure_process_killed
    from sources.functions.ensure_py_system_process_ran_by_pnx import ensure_py_system_process_ran_by_pnx
    from sources.functions.ensure_slept import ensure_slept
    from sources.functions.ensure_value_completed_advanced import ensure_value_completed_advanced
    from sources.functions.get_nx import get_nx
    from sources.functions.get_os_n import get_os_n
    from sources.functions.get_pnxs import get_pnxs
    from sources.functions.get_set_from_list import get_set_from_list
    from sources.functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd
    from sources.functions.is_process_killed import is_process_killed
    from sources.objects.pk_etc import PK_USERLESS_LINE
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_map_texts import PkTexts
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_WRAPPERS

    try:

        if get_os_n() == 'windows':
            ensure_chcp_65001()
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()

        windows_opened = get_set_from_list(get_windows_opened_with_hwnd())

        mode = PkTexts.FILE_GEN_TIME_STABLE_MODE

        key_name = 'directory_to_monitor'
        directories = get_pnxs(d_working=D_TASK_ORCHESTRATOR_CLI_SOURCES, filtered="d")
        directory_to_monitor = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=directories)
        directory_to_monitor = Path(directory_to_monitor)
        logging.debug(f'''directory_to_monitor={directory_to_monitor} {'%%%FOO%%%' if LTA else ''}''')

        # key_name = 'file_to_monitor'
        # files = get_pnxs(d_working=D_TASK_ORCHESTRATOR_CLI_FUNCTIONS, filtered="f")
        # files += get_pnxs(d_working=D_TASK_ORCHESTRATOR_CLI_RESOURCES, filtered="f")
        # file_to_monitor = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=files)
        # file_to_monitor = Path(file_to_monitor)
        # logging.debug(f'''file_to_monitor={file_to_monitor} {'%%%FOO%%%' if LTA else ''}''')

        key_name = 'file_to_execute'
        files = get_pnxs(d_working=D_TASK_ORCHESTRATOR_CLI_WRAPPERS, filtered="f")
        file_to_execute = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=files)
        file_to_execute = Path(file_to_execute)
        logging.debug(f'''file_to_execute={file_to_execute} {'%%%FOO%%%' if LTA else ''}''')

        files_to_monitor = [
                               # file_to_monitor,
                           ] + get_pnxs(d_working=directory_to_monitor, filtered="f")
        files_to_execute = [
            file_to_execute,
        ]
        loop_cnt = 1

        # task_orchestrator_cli_option
        # key_name = 'stable_seconds_limit'
        # stable_seconds_limit = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=[1, 2,3,4,5,6,10])
        stable_seconds_limit = 2

        window_title_to_kill = None
        file_to_execute = None
        if mode == PkTexts.FILE_GEN_TIME_STABLE_MODE:
            while 1:
                # ensure_console_cleared()

                if loop_cnt == 1:
                    ensure_spoken(f"핫리로더 시작...")
                    print(f"핫리로더 시작...")
                    for file_to_execute in files_to_execute:
                        file_to_execute = Path(file_to_execute)
                        logging.debug(f'''f={file_to_execute} {'%%%FOO%%%' if LTA else ''}''')
                        windows_opened.add(get_nx(file_to_execute))
                        file_to_execute = file_to_execute
                        window_title_to_kill = get_nx(file_to_execute)  # task_orchestrator_cli_option
                        ensure_py_system_process_ran_by_pnx(file_to_execute=file_to_execute, mode='a')
                    loop_cnt = loop_cnt + 1
                    continue

                logging.debug(PK_USERLESS_LINE)

                if not ensure_files_modified_time_stable(files_to_monitor=files_to_monitor, monitoring_seconds=stable_seconds_limit):
                    ensure_spoken(f"edited 감지")
                    logging.debug(f"핫리로더, {stable_seconds_limit} 초, 중에 not stable 감지")
                    if ensure_files_modified_time_stable(files_to_monitor=files_to_monitor, monitoring_seconds=stable_seconds_limit):
                        ensure_spoken(f"edit complete 감지")
                        logging.debug(f"핫리로더, {stable_seconds_limit} 초, 동안 stable 감지")
                        for file_to_execute in files_to_execute:
                            ensure_process_killed(window_title_seg=window_title_to_kill)
                            ensure_slept(milliseconds=80)
                            ensure_py_system_process_ran_by_pnx(file_to_execute=file_to_execute, mode='a')
                            logging.debug(f"리로드 시도완료")
                            ensure_spoken(f"", wait=True)
                else:
                    logging.debug(f"{stable_seconds_limit} 초 동안 stable 감지 완료")

                ensure_slept(milliseconds=80)
                # time.sleep(80)  # 로깅 방지

                # task_orchestrator_cli_option
                ensure_task_orchestrator_cli_useless_log_removed(text=PK_USERLESS_LINE)

    except:
        ensure_debug_loged_verbose(traceback)
