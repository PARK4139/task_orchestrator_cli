from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_colorama_initialized_once():
    from colorama import init as pk_colorama_init
    # pk_colorama_init(autoreset=True)
    pk_colorama_init(autoreset=True, strip=False, convert=False)
