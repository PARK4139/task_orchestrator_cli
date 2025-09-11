from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_gemini_cli_expected_titles():
    from functions.get_os_sys_environment_variable import get_os_sys_environment_variable

    options = [
        f"Gemini - {get_os_sys_environment_variable("USERNAME")}",
        "Gemini - task_orchestrator_cli",
        "Windows PowerShell",
        "pk_ensure_gemini_cli_worked_done.py",  # 어떻게 이런 것들이 있지? -> gemini가 대신 실행해주면 이렇게 창이름이 바뀜
    ]
    return options
