from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.functions.ensure_target_enabled import ensure_target_enabled


@ensure_seconds_measured
def ensure_vscode_enabled():
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from sources.objects.task_orchestrator_cli_files import F_VSCODE_LNK
    ensure_target_enabled(F_VSCODE_LNK, D_TASK_ORCHESTRATOR_CLI)
