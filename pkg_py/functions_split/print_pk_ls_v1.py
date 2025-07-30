def print_pk_ls_v1():
    from pkg_py.functions_split.get_pnx_working_with_idx_option import get_pnx_working_with_idx_option
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_pnxs import get_pnxs
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.directories import D_PKG_PY

    pnx_list = get_pnxs(d_working=D_PKG_PY, with_walking=0)
    list_b = [rf"{D_PKG_PY}/__init__.py", f"{D_PKG_PY}/__pycache__"]
    list_b = [get_pnx_os_style(element) for element in list_b]
    pnx_working_with_idx_dict = get_pnx_working_with_idx_option(origin_list=pnx_list, minus_list=list_b)

    if LTA:
        ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''')
    for idx, pnx_working in enumerate(pnx_working_with_idx_dict):
        print(f'pk {idx} {get_nx(pnx_working_with_idx_dict[idx])}')
