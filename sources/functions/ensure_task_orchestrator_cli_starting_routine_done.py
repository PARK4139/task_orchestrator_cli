from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_starting_routine_done(*, __file__, traceback):
    from sources.functions.ensure_task_orchestrator_cli_colorama_initialized_once import ensure_task_orchestrator_cli_colorama_initialized_once
    from sources.functions.ensure_task_orchestrator_cli_log_initialized import ensure_task_orchestrator_cli_log_initialized
    from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
    from sources.functions.ensure_task_orchestrator_cli_wrapper_window_title_replaced import ensure_task_orchestrator_cli_wrapper_window_title_replaced

    # pk_option
    # if is_os_windows():
    #     ensure_chcp_65001()

    ensure_task_orchestrator_cli_wrapper_suicided(__file__)
    ensure_task_orchestrator_cli_colorama_initialized_once()
    ensure_task_orchestrator_cli_log_initialized(__file__)
    ensure_task_orchestrator_cli_wrapper_window_title_replaced(__file__)
