def is_os_linux():
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    if not is_os_wsl_linux():
        if not is_os_windows():
            return True
    return False
