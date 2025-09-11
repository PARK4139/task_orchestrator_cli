def ensure_console_cleared():
    from sources.functions.is_os_windows import is_os_windows

    if is_os_windows():
        import os
        os.system('cls')
    else:
        os.system('clear')
