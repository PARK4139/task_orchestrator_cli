from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_python_file_executed_in_uv_venv_windows(python_file):
    from functions.ensure_command_executed import ensure_command_executed
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from objects.task_orchestrator_cli_files import F_VENV_PYTHON_EXE, F_VENV_ACTIVATE_BAT

    return ensure_command_executed(rf'start "" cmd.exe /c "cd /d "{D_TASK_ORCHESTRATOR_CLI}" && {F_VENV_ACTIVATE_BAT} && {F_VENV_PYTHON_EXE} "{python_file}"', mode='a')
