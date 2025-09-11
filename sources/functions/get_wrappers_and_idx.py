def get_wrappers_and_idx():
    from sources.functions.get_pnx_working_with_idx_option import get_pnx_working_with_idx_option
    from sources.functions.get_pnxs import get_pnxs
    from pathlib import Path
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
    origin_list = get_pnxs(d_working=D_TASK_ORCHESTRATOR_CLI_RESOURCES, with_walking=0)
    minus_list = [rf"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/__init__.py", f"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/__pycache__"]
    minus_list = [Path(pnx) for pnx in minus_list]
    return get_pnx_working_with_idx_option(origin_list=origin_list, minus_list=minus_list)
