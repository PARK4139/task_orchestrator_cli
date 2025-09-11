def ensure_task_orchestrator_cli_useless_log_removed(text, loop_mode=False):
    import logging
    from sources.functions import ensure_slept
    from sources.functions.ensure_last_lines_removed_from_file import ensure_last_lines_removed_from_file
    from sources.functions.get_line_number_from_file import get_line_number_from_file
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.task_orchestrator_cli_files import F_TASK_ORCHESTRATOR_CLI_LOG
    if LTA:
        if loop_mode == True:
            while 1:
                line_number = get_line_number_from_file(text=text, from_reverse_mode=True, file_path=F_TASK_ORCHESTRATOR_CLI_LOG)
                if line_number:
                    if int(line_number):
                        ensure_last_lines_removed_from_file(file=F_TASK_ORCHESTRATOR_CLI_LOG, lines_to_remove_from_end=line_number)
                        return True
                ensure_slept(milliseconds=80)

        else:
            line_number = get_line_number_from_file(text=text, from_reverse_mode=True, file_path=F_TASK_ORCHESTRATOR_CLI_LOG)
            if line_number is not None:
                ensure_last_lines_removed_from_file(file=F_TASK_ORCHESTRATOR_CLI_LOG, lines_to_remove_from_end=int(line_number))
                logging.debug(rf"line_number={line_number}")
                return True
            else:
                logging.debug(f"Text '{text[:10]}...' not found in log file. No lines removed.")
                return False
