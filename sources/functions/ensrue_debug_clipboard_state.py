from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensrue_debug_clipboard_state():
    # code for fixing 클립보드 삭제 이슈
    import logging
    import logging
    from sources.objects.pk_local_test_activate import LTA
    from sources.functions.get_clipboard_text import get_clipboard_text
    from sources.functions.ensure_task_orchestrator_cli_log_initialized import ensure_task_orchestrator_cli_log_initialized
    ensure_task_orchestrator_cli_log_initialized(__file__)
    logging.debug(get_clipboard_text())
    logging.debug(f'''get_clipboard_text()={get_clipboard_text()} {'%%%FOO%%%' if LTA else ''}''')
    import sys
    sys.exit()
