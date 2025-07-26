

def kill_self_pk_program(self_f):
    # code for pk program, suicide
    
    from pkg_py.system_object.directories import D_PKG_PY
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_ps1.system_object.process import kill_process_by_window_title_seg

    f_list = [
        rf"{D_PKG_PY}/{get_nx(self_f)}",
    ]
    f_list = get_list_that_element_applyed_via_func(func=get_pnx_os_style, working_list=f_list)
    for f in f_list:
        pk_kill_process_by_window_title_seg(window_title_seg=get_nx(f))
