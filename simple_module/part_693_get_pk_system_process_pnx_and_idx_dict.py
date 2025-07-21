from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def get_pk_system_process_pnx_and_idx_dict():
    pnx_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0)
    list_b = [rf"{D_PKG_PY}/__init__.py", f"{D_PKG_PY}/__pycache__"]
    list_b = [get_pnx_os_style(element) for element in list_b]
    pk_system_process_pnx_and_idx_dict = get_TBD_pnx_working_with_idx_dict(origin_list=pnx_list, minus_list=list_b)
    return pk_system_process_pnx_and_idx_dict
