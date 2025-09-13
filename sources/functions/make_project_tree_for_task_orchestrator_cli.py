from functions import ensure_pnx_made

from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES


def make_project_tree_for_task_orchestrator_cli():
    leaf_directories = [
        D_TASK_ORCHESTRATOR_CLI_RESOURCES
    ]
    for leaf_directory in leaf_directories:
        ensure_pnx_made(pnx=leaf_directory, mode="d")
    leaf_files = [
        # ...
    ]
    for leaf_file in leaf_files:
        ensure_pnx_made(pnx=leaf_file, mode="f")
