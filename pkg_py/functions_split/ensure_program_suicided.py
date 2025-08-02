def ensure_program_suicided(self_f):
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.functions_split.ensure_process_killed_by_window_title import ensure_process_killed_by_window_title
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    ensure_printed(f'''[{PkMessages2025.DATA}] self_f={self_f} {'%%%FOO%%%' if LTA else ''}''')
    ensure_process_killed_by_window_title(window_title=get_nx(get_pnx_os_style(self_f)))
