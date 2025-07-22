def print_pk_ls_v1():
    from pkg_py.functions_split.get_TBD_pnx_working_with_idx_dict import get_TBD_pnx_working_with_idx_dict
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_pnx_list import get_pnx_list
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.pk_system_object.directories import D_PKG_PY

    pnx_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0)
    list_b = [rf"{D_PKG_PY}/__init__.py", f"{D_PKG_PY}/__pycache__"]
    list_b = [get_pnx_os_style(element) for element in list_b]
    pnx_working_with_idx_dict = get_TBD_pnx_working_with_idx_dict(origin_list=pnx_list, minus_list=list_b)

    if LTA:
        pk_print(f'''{'%%%FOO%%%' if LTA else ''}''')
    for idx, pnx_working in enumerate(pnx_working_with_idx_dict):
        print(f'pk {idx} {get_nx(pnx_working_with_idx_dict[idx])}')
