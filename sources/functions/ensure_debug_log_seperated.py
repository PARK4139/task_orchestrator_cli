from functions.ensure_debug_loged_simple import ensure_debug_loged_simple
from sources.objects.pk_etc import PK_UNDERLINE, PK_DEBUG_LINE


def ensure_log_seperated_by_pk_debug_line(func):
    from sources.functions.ensure_task_orchestrator_cli_cleared import ensure_task_orchestrator_cli_cleared
    from sources.functions import ensure_console_cleared
    from sources.objects.pk_local_test_activate import LTA
    import logging
    from functools import wraps
    if not LTA:
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        ensure_console_cleared()
        ensure_task_orchestrator_cli_cleared()
        logging.debug(PK_DEBUG_LINE)

        result = func(*args, **kwargs)

        logging.debug(PK_DEBUG_LINE)
        return result

    return wrapper
