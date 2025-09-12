from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_pycharm_opened():
    from sources.functions.get_execute_cmd_with_brakets import get_cmd_chains
    from sources.functions.ensure_command_executed import ensure_command_executed

    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from sources.objects.task_orchestrator_cli_files import F_PYCHARM64_EXE

    ensure_command_executed(cmd=f'start "" {get_cmd_chains(F_PYCHARM64_EXE, D_TASK_ORCHESTRATOR_CLI)}', mode='a')
