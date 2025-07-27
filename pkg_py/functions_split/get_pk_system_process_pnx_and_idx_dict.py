def get_pk_system_process_pnx_and_idx_dict():
    from pkg_py.functions_split.get_TBD_pnx_working_with_idx_dict import get_TBD_pnx_working_with_idx_dict
    from pkg_py.functions_split.get_pnxs import get_pnxs
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.directories import D_PKG_PY
    pnx_list = get_pnxs(d_working=D_PKG_PY, with_walking=0)
    list_b = [rf"{D_PKG_PY}/__init__.py", f"{D_PKG_PY}/__pycache__"]
    list_b = [get_pnx_os_style(element) for element in list_b]
    pk_system_process_pnx_and_idx_dict = get_TBD_pnx_working_with_idx_dict(origin_list=pnx_list, minus_list=list_b)
    return pk_system_process_pnx_and_idx_dict
