from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_claude_enabled():
    from pathlib import Path

    from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI

    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.objects.task_orchestrator_cli_files import F_CLAUDE_LNK
    file_exe = Path(F_CLAUDE_LNK)
    ensure_command_executed(cmd=f'start "" "{file_exe}" "{D_TASK_ORCHESTRATOR_CLI}"')
