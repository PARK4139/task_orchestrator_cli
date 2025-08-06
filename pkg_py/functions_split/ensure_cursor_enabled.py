def ensure_cursor_enabled():
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    from pkg_py.system_object.directories  import D_PROJECT

    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.system_object.files import F_CURSOR_EXE
    file_exe = get_pnx_os_style(F_CURSOR_EXE)
    ensure_command_excuted_to_os(cmd=f'start "" "{file_exe}" "{D_PROJECT}"', mode="a")
