import logging


def ensure_status_printed_step(step_num: int, cmd: str, code: int, output: str) -> str:
    from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
    if code == 0:
        label, color = "SUCCESS", TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['CYAN']
    elif "nothing to commit" in output.lower():
        label, color = "SKIPPED", TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['YELLOW']
    elif "everything up-to-date" in output.lower():
        label, color = "SKIPPED", TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['YELLOW']
    else:
        label, color = "FAILED", TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RED']
    logging.debug(f"[ {color}{label}{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']} ] [STEP {step_num}] {cmd}")
    return label


