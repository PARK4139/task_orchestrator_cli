
def get_text_cyan(text):
    from objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
    cyan_text = f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['CYAN']}{text}{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}"
    return cyan_text
