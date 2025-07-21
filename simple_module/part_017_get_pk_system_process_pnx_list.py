

def get_pk_system_process_pnx_list():
    from pkg_py.pk_system_layer_directories import D_PKG_PY
    from pkg_py.simple_module.part_005_get_nx import get_nx
    from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
    from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
    from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
    pnx_filtered = []
    pnx_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0)
    pnx_to_except = [rf"{D_PKG_PY}/__init__.py", f"{D_PKG_PY}/__pycache__"]
    pnx_to_except = [get_pnx_os_style(element) for element in pnx_to_except]
    pnx_excepted = get_list_calculated(origin_list=pnx_list, minus_list=pnx_to_except)
    for pnx in pnx_excepted:
        filename = get_nx(pnx)
        if filename.startswith("pk_"):
            # print(filename)
            pnx_filtered.append(pnx)
    return pnx_filtered
