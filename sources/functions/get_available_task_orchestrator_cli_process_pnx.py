def get_available_task_orchestrator_cli_process_pnx(pk_idx):
    from sources.functions.get_wrappers_and_idx import get_wrappers_and_idx
    task_orchestrator_cli_process_pnxs_and_idx = get_wrappers_and_idx()
    return task_orchestrator_cli_process_pnxs_and_idx[pk_idx]
