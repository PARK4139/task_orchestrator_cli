

from sources.functions.get_idx_list import get_idx_list
from sources.functions.get_task_orchestrator_cli_process_pnxs import get_task_orchestrator_cli_process_pnxs


def get_task_orchestrator_cli_process_available_idx_list():
    pk_python_pnx_working_without_idx_list = get_task_orchestrator_cli_process_pnxs()
    pnx_working_idx_list = get_idx_list(item_iterable=pk_python_pnx_working_without_idx_list)
    pnx_working_idx_list = list(map(str, pnx_working_idx_list))  # each (element ->> str(element))
    return pnx_working_idx_list
