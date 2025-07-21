

from pkg_py.simple_module.part_008_get_idx_list import get_idx_list
from pkg_py.simple_module.part_017_get_pk_system_process_pnx_list import get_pk_system_process_pnx_list


def get_pk_system_process_available_idx_list():
    pk_python_pnx_working_without_idx_list = get_pk_system_process_pnx_list()
    pnx_working_idx_list = get_idx_list(item_iterable=pk_python_pnx_working_without_idx_list)
    pnx_working_idx_list = list(map(str, pnx_working_idx_list))  # each (element ->> str(element))
    return pnx_working_idx_list
