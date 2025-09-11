from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_wrapper_window_title_replaced(window_title):
    from sources.functions.get_nx import get_nx
    from sources.functions.ensure_window_title_replaced import ensure_window_title_replaced


    ensure_window_title_replaced(get_nx(window_title))
