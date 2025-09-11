from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_memo_editable():
    from functions.ensure_command_executed import ensure_command_executed
    from functions.get_execute_cmd_with_brakets import get_cmd_chains
    import logging
    import traceback
    from sources.objects.task_orchestrator_cli_files import F_MEMO_WORKING_MD
    try:
        # ensure_target_enabled(F_VSCODE, F_MEMO_WORKING_MD)
        ensure_command_executed(cmd=f'start "" {get_cmd_chains(F_MEMO_WORKING_MD)}')
    except:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
