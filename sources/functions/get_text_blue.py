def get_text_blue(text: str) -> str:
    from objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
    blue_text = f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP["BLUE"]}{text}{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP["RESET"]}"
    return blue_text
