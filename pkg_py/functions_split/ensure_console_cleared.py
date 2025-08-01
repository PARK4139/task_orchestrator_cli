def ensure_console_cleared():
    from pkg_py.functions_split.is_os_windows import is_os_windows

    if is_os_windows():
        import os
        os.system('cls')
