
import logging

def ensure_url_opened(url: str):
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.ensure_task_orchestrator_cli_log_initialized import ensure_task_orchestrator_cli_log_initialized

    ensure_task_orchestrator_cli_log_initialized(__file__)

    if not isinstance(url, str) or not (url.startswith('http://') or url.startswith('https://')):
        logging.error(f"유효하지 않은 URL입니다: {url}")
        return

    logging.info(f"Opening URL: {url}")
    cmd = f"explorer {url}"
    ensure_command_executed(cmd, mode="a") # 비동기 모드로 실행하여 즉시 반환

