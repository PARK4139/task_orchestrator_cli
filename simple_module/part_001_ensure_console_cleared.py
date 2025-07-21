

from pkg_py.simple_module.part_002_is_os_windows import is_os_windows


def ensure_console_cleared():
    if is_os_windows():
        import os
        os.system('cls')
