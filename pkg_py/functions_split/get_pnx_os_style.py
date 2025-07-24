def get_pnx_os_style(pnx):
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
    from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
    from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

    if is_os_wsl_linux():
        pnx = get_pnx_wsl_unix_style(pnx=pnx)
        return pnx
    if is_os_windows():
        pnx = get_pnx_windows_style(pnx=pnx)
        return pnx
    else:
        pnx = get_pnx_unix_style(pnx=pnx)
        return pnx
