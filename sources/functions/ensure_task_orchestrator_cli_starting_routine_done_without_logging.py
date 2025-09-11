from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_starting_routine_done_without_logging(*, __file__, traceback):
    from functions.ensure_task_orchestrator_cli_log_initialized import ensure_task_orchestrator_cli_log_initialized
    from sources.functions.ensure_task_orchestrator_cli_colorama_initialized_once import ensure_task_orchestrator_cli_colorama_initialized_once
    from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
    from sources.functions.ensure_task_orchestrator_cli_wrapper_window_title_replaced import ensure_task_orchestrator_cli_wrapper_window_title_replaced

    ensure_task_orchestrator_cli_wrapper_suicided(__file__)
    ensure_task_orchestrator_cli_colorama_initialized_once()
    ensure_task_orchestrator_cli_wrapper_window_title_replaced(__file__)
    ensure_task_orchestrator_cli_log_initialized(__file__, with_file_logging_mode=False)
