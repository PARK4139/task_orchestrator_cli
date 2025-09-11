def is_os_linux():
    from sources.functions.is_os_wsl_linux import is_os_wsl_linux
    from sources.functions.is_os_windows import is_os_windows
    if not is_os_wsl_linux():
        if not is_os_windows():
            return True
    return False
