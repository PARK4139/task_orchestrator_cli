from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_routine_gemini_cli_assistance_enabled():
    import os

    from functions.ensure_spoken import ensure_spoken
    from functions.ensure_gemini_cli_enabled_interactive import ensure_gemini_cli_enabled_interactive
    from functions.ensure_gemini_cli_assistance_enabled import ensure_gemini_cli_assistance_enabled
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI

    os.chdir(D_TASK_ORCHESTRATOR_CLI)  # GEMINI.md 위치 로 이동

    ensure_gemini_cli_enabled_interactive(__file__)

    ensure_gemini_cli_assistance_enabled()

    ensure_spoken(f'', wait=True)  # pk_❤  pk_🩵  pk_🤍



