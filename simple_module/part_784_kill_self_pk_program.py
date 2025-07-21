

def kill_self_pk_program(self_f):
    # code for pk program, suicide
    from pkg_py.simple_module.part_783_get_list_that_element_applyed_via_func import \
        get_list_that_element_applyed_via_func
    from pkg_py.pk_system_layer_directories import D_PKG_PY
    from pkg_py.simple_module.part_005_get_nx import get_nx
    from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
    from pkg_ps1.pk_system_layer_100_process import pk_kill_process_by_window_title_seg

    f_list = [
        rf"{D_PKG_PY}/{get_nx(self_f)}",
    ]
    f_list = get_list_that_element_applyed_via_func(func=get_pnx_os_style, working_list=f_list)
    for f in f_list:
        pk_kill_process_by_window_title_seg(window_title_seg=get_nx(f))
