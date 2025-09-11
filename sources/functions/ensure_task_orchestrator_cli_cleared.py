from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_cleared():
    from sources.objects.task_orchestrator_cli_files import F_TASK_ORCHESTRATOR_CLI_LOG
    from sources.functions.ensure_file_cleared import ensure_file_cleared
    from sources.functions.ensure_task_orchestrator_cli_log_initialized import ensure_task_orchestrator_cli_log_initialized

    logging_file = F_TASK_ORCHESTRATOR_CLI_LOG

    # 중복 초기화 방지를 위한 플래그 체크
    if hasattr(ensure_task_orchestrator_cli_log_initialized, '_initialized'):
        return
    ensure_task_orchestrator_cli_log_initialized._initialized = True

    ensure_file_cleared(logging_file)
