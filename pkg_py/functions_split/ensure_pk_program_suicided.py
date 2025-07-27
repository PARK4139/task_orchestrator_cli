def ensure_pk_program_suicided(self_f):
    from pkg_py.functions_split.ensure_process_killed_by_window_title_seg import ensure_process_killed_by_window_title_seg
    from pkg_py.functions_split.get_list_that_element_applyed_via_func import get_list_that_element_applyed_via_func

    # code for pk program, suicide

    from pkg_py.system_object.directories import D_PKG_PY
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    f_list = [
        rf"{D_PKG_PY}/{get_nx(self_f)}",
    ]
    f_list = get_list_that_element_applyed_via_func(func=get_pnx_os_style, working_list=f_list)
    for f in f_list:
        ensure_process_killed_by_window_title_seg(window_title_seg=get_nx(f))
