import logging

from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_log_blocked():
    logger = logging.getLogger()
    logger.debug("task_orchestrator_cli logging is now blocked.")
    logger.handlers.clear()
    logging.disable(logging.CRITICAL + 1)
