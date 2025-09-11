

def ensure_end_time_logged():
    from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
    import time
    end_time = time.time()
    GREEN = TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['CYAN']
    RESET = TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']
    print(f"ENDED AT : {GREEN}{time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
    return end_time


