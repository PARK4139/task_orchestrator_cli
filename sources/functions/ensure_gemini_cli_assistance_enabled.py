from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_cli_assistance_enabled():
    from functions.ensure_spoken import ensure_spoken
    from functions.ensure_task_orchestrator_cli_python_file_executed_in_uv_venv_windows import ensure_task_orchestrator_cli_python_file_executed_in_uv_venv_windows
    from functions.get_gemini_prompt_interface_title import get_gemini_cli_assistance_title
    from functions.is_gemini_cli_assistance_opened import is_gemini_cli_assistance_opened
    from functions.is_window_opened_via_window_title import is_window_opened_via_window_title
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_WRAPPERS
    from sources.functions.ensure_window_maximized_like_human import ensure_window_maximized_like_human
    from sources.functions.ensure_window_to_front import ensure_window_to_front

    opened = is_gemini_cli_assistance_opened()
    gemini_cli_assistance_title = get_gemini_cli_assistance_title()
    if not opened:
        ensure_spoken(f'gemini whip 종료되어있습니다.')
        ensure_spoken(f'실행을 시도합니다')
        ensure_task_orchestrator_cli_python_file_executed_in_uv_venv_windows(python_file=D_TASK_ORCHESTRATOR_CLI_WRAPPERS / "pk_ensure_gemini_cli_assistance_executed.py")
    else:
        if is_window_opened_via_window_title(gemini_cli_assistance_title):
            ensure_spoken(f'gemini whip 가 이미 실행중입니다.')
            ensure_window_to_front(gemini_cli_assistance_title)
            ensure_window_maximized_like_human()
            ensure_spoken(f'', wait=True)
            return
