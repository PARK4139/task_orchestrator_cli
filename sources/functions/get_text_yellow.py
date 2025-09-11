def get_text_yellow(text: str) -> str:
    from objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
    yellow_text = f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP["YELLOW"]}{text}{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP["RESET"]}"
    return yellow_text
