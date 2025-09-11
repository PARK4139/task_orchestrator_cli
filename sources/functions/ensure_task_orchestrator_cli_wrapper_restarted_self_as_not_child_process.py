from functions.ensure_guided_not_prepared_yet import ensure_not_prepared_yet_guided
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_python_file_enabled_advanced(file_path, not_child_process_mode = True):
    from sources.functions.get_nx import get_nx
    import logging

    from sources.functions import is_pnx_existing
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_WRAPPERS
    from pathlib import Path

    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.objects.task_orchestrator_cli_files import F_VENV_ACTIVATE_BAT, F_VENV_PYTHON_EXE

    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    target_file = Path(file_path)
    if is_pnx_existing(target_file):
        if not_child_process_mode == True:
            cmd = rf'start "" cmd.exe /c "cd /d "{D_TASK_ORCHESTRATOR_CLI}" && {F_VENV_ACTIVATE_BAT} && {F_VENV_PYTHON_EXE} "{target_file}"'
            logging.debug(rf'cmd={cmd}')
            return ensure_command_executed(cmd, mode='a')
        else:
            ensure_not_prepared_yet_guided()


