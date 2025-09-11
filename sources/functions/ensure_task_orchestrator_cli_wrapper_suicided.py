# @ensure_seconds_measured
def ensure_task_orchestrator_cli_wrapper_suicided(file_path):
    import logging
    from sources.objects.pk_local_test_activate import LTA
    from sources.functions.ensure_process_killed_by_window_title import ensure_process_killed_by_window_title
    from sources.functions.get_nx import get_nx
    from pathlib import Path
    logging.debug(f'''file_path={file_path} {'%%%FOO%%%' if LTA else ''}''')
    ensure_process_killed_by_window_title(window_title=get_nx(Path(file_path)))
