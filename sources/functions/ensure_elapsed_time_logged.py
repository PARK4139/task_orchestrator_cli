def ensure_elapsed_time_logged(start_time, log_file_path=None):
    from sources.functions.print_and_save_log_to_file import print_and_save_log_to_file
    from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
    import time
    from sources.objects.pk_map_texts import PkTexts
    import inspect
    from sources.objects.task_orchestrator_cli_directories import D_DESKTOP

    if log_file_path is None:
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()
        log_file_default = f"{D_DESKTOP}/result_of_{func_n}.txt"
        log_file_path = log_file_default
    duration = time.time() - start_time
    elapsed_time = rf"{duration:.2f}"
    msg = f"{TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['YELLOW']}ENDED AT : {duration:.2f} {PkTexts.SECONDS} {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}"
    print_and_save_log_to_file(msg, log_file_path)

    # task_orchestrator_cli_option
    # print_marker_and_stop()

    # task_orchestrator_cli_option
    # ensure_task_orchestrator_cli_exit_silent()
    return elapsed_time
