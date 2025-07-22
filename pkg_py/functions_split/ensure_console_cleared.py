

from pkg_py.functions_split.is_os_windows import is_os_windows


def ensure_console_cleared():
    if is_os_windows():
        import os
        os.system('cls')
