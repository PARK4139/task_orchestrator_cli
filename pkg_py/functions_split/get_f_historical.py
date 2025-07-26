from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def get_history_file(file_id):
    import os
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025

    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.directories import D_PKG_HISTORY

    history_file = f"{D_PKG_HISTORY}/{file_id}.history"
    history_file = get_pnx_os_style(history_file)
    ensure_pnx_made(pnx=history_file, mode="f")
    ensure_printed(f'''[{PkMessages2025.DATA}] does_pnx_exist(history_file)={does_pnx_exist(history_file)} {'%%%FOO%%%' if LTA else ''}''')

    ensure_printed(f'''[{PkMessages2025.DATA}] history_file={history_file} {'%%%FOO%%%' if LTA else ''}''')
    return history_file
