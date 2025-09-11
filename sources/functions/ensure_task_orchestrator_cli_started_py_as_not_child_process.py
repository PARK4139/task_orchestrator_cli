from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_started_py_as_not_child_process():
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.objects.task_orchestrator_cli_files import F_VENV_ACTIVATE_BAT, F_PK_ENSURE_TASK_ORCHESTRATOR_CLI_STARTED_PY, \
        F_VENV_PYTHON_EXE

    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI

    return ensure_command_executed(
        rf'start "" cmd.exe /c "cd /d "{D_TASK_ORCHESTRATOR_CLI}" && {F_VENV_ACTIVATE_BAT} && {F_VENV_PYTHON_EXE} "{F_PK_ENSURE_TASK_ORCHESTRATOR_CLI_STARTED_PY}"',
        mode='a')
