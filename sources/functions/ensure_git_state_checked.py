def ensure_git_state_checked(start_time, label):
    import logging
    import time

    from sources.functions.run_command import run_command
    from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP

    cmd = "git status"
    _, output = run_command(cmd, capture_output=True)
    output = output.split("\n")
    for _ in output:
        logging.debug(f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['YELLOW']}{_}{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")
    duration = time.time() - start_time
    logging.debug(f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['YELLOW']}{label}{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']} at {time.strftime('%Y-%m-%d %H:%M:%S')} (elapsed {duration:.2f} sec)")
    return False

