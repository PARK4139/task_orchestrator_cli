def get_task_orchestrator_cli_process_nxs():
    from sources.functions.get_list_calculated import get_list_calculated
    from sources.functions.get_nx import get_nx
    from pathlib import Path
    from sources.functions.get_pnxs import get_pnxs
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
    nx_filtered = []
    pnx_list = get_pnxs(d_working=D_TASK_ORCHESTRATOR_CLI_RESOURCES, with_walking=0)
    pnx_to_except = [rf"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/__init__.py", f"{D_TASK_ORCHESTRATOR_CLI_RESOURCES}/__pycache__"]
    pnx_to_except = [Path(element) for element in pnx_to_except]
    pnx_excepted = get_list_calculated(origin_list=pnx_list, minus_list=pnx_to_except)
    for pnx in pnx_excepted:
        filename = get_nx(pnx)
        if filename.startswith("pk_"):
            # print(filename)
            nx_filtered.append(filename)
    return nx_filtered
