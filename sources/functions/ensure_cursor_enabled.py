from sources.functions.ensure_target_enabled import ensure_target_enabled


def ensure_cursor_enabled():
    from sources.functions.get_execute_cmd_with_brakets import get_cmd_chains
    from sources.functions.get_nx import get_nx
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.is_window_opened import is_window_opened
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.objects.task_orchestrator_cli_files import F_CURSOR_LNK


    ensure_target_enabled(F_CURSOR_LNK, D_TASK_ORCHESTRATOR_CLI)