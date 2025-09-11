from enum import Enum


def print_prompt_via_colorama(prompt: str, colorama_code: str, flush, line_feed_mode=1):
    from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP

    color_code = TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP.get(colorama_code, TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET'])
    end_char = '' if line_feed_mode == 0 else '\n'
    print(f"{color_code}{prompt}", end=end_char, flush=flush)
