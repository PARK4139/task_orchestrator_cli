from functions.ensure_target_enabled import ensure_target_enabled
from functions.ensure_window_to_front import ensure_window_to_front
from objects.task_orchestrator_cli_files import F_PYCHARM64_EXE
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_log_editable():
    from functions import ensure_command_executed
    from sources.objects.task_orchestrator_cli_files import F_TASK_ORCHESTRATOR_CLI_LOG

    # ensure_target_enabled(editor=F_VSCODE, target=F_TASK_ORCHESTRATOR_CLI_LOG, mode='a')
    # ensure_target_enabled(editor=F_PYCHARM, target=F_TASK_ORCHESTRATOR_CLI_LOG, mode='a')
    # title = f"{get_nx(F_TASK_ORCHESTRATOR_CLI_LOG)} - Visual Studio Code"
    # ensure_command_executed(cmd=f'start "" {F_TASK_ORCHESTRATOR_CLI_LOG}')
    ensure_command_executed(cmd=f'start "" explorer.exe {F_TASK_ORCHESTRATOR_CLI_LOG}')
    ensure_window_to_front(window_title_seg=F_TASK_ORCHESTRATOR_CLI_LOG)
    # ensure_window_minimized(window_title=title)
