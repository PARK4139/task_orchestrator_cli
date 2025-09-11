def ensure_finally_routine_done(*, D_TASK_ORCHESTRATOR_CLI, __file__):
    from sources.functions.ensure_task_orchestrator_cli_log_blocked import ensure_task_orchestrator_cli_log_blocked
    from sources.objects.pk_local_test_activate import LTA

    from sources.functions.ensure_spoken import get_pk_spoken_manager

    import logging
    from sources.objects.pk_etc import PK_UNDERLINE

    # task_orchestrator_cli_option
    ensure_task_orchestrator_cli_log_blocked()

    logging.debug(PK_UNDERLINE)
    if LTA:
        # task_orchestrator_cli_option
        exceptions = [
            "pk_ensure_snipping_tool_exe_opened.py",
            "pk_ensure_test_scenarios_executed.py",
        ]

        if not any(name in __file__ for name in exceptions):
            # ensure_task_orchestrator_cli_log_editable() # pk_option
            pass
        # ensure_cursor_enabled()
        # ensure_windows_printed()
        # ensure_pycharm_opened()
        pass

    if not LTA:
        script_to_run = rf"{D_TASK_ORCHESTRATOR_CLI}\.venv_windows\Scripts\activate && python {__file__} && deactivate"
        logging.debug(PK_UNDERLINE)
        logging.debug(f"'[ TRY GUIDE ]' {script_to_run}")
        logging.debug(PK_UNDERLINE)

    get_pk_spoken_manager()._queue.join()  # 완전히 재생될때 까지 # 모든 큐 작업이 완료될 때까지 flow 더 흘러가지 못하도록, 블로킹
    get_pk_spoken_manager().terminate()  # 리소스 해제

    # task_orchestrator_cli_option : remove useless lines from end of file
    # ensure_task_orchestrator_cli_useless_log_removed(text=PK_UNDERLINE)
