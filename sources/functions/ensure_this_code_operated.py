from types import ModuleType


def ensure_this_code_operated(ipdb: ModuleType):
    from sources.functions.ensure_task_orchestrator_cli_log_editable import ensure_task_orchestrator_cli_log_editable
    import logging
    from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP

    # based on from types import ModuleType
    logging.debug(f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['CYAN']}here! here! here! here! here! here! here! here! here! here! here! here! {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")
    ensure_task_orchestrator_cli_log_editable(ipdb)
