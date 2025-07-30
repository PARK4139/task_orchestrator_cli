def get_pk_system_processes_and_idx():
    from pkg_py.functions_split.get_pnx_working_with_idx_option import get_pnx_working_with_idx_option
    from pkg_py.functions_split.get_pnxs import get_pnxs
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.directories import D_PKG_PY
    origin_list = get_pnxs(d_working=D_PKG_PY, with_walking=0)
    minus_list = [rf"{D_PKG_PY}/__init__.py", f"{D_PKG_PY}/__pycache__"]
    minus_list = [get_pnx_os_style(pnx) for pnx in minus_list]
    return get_pnx_working_with_idx_option(origin_list=origin_list, minus_list=minus_list)
