def ensure_pk_program_suicided(self_f):
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.functions_split.ensure_process_killed_by_window_title_seg import ensure_process_killed_by_window_title_seg
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    # pk_program = get_list_that_element_applyed_via_func(func=get_pnx_os_style, working_list=rf"{D_PKG_PY}/{get_nx(self_f)}", )

    ensure_printed(f'''[{PkMessages2025.DATA}] self_f={self_f} {'%%%FOO%%%' if LTA else ''}''')
    ensure_process_killed_by_window_title_seg(window_title_seg=get_nx(get_pnx_os_style(self_f)))
