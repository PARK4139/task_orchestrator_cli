

from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style


def get_pnx_os_style(pnx):
    if is_os_wsl_linux():
        pnx = get_pnx_wsl_unix_style(pnx=pnx)
        return pnx
    if is_os_windows():
        pnx = get_pnx_windows_style(pnx=pnx)
        return pnx
    else:
        pnx = get_pnx_unix_style(pnx=pnx)
        return pnx
