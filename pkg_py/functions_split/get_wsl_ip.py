

# import pywin32

from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.pk_print import pk_print


def get_wsl_ip(wsl_distro_n):
    if is_os_windows():
        std_out_list = cmd_to_os(rf'wsl -d {wsl_distro_n} hostname -I', encoding='utf-8')
    else:
        if is_os_wsl_linux():
            std_out_list = cmd_to_os(rf'hostname -I', encoding='utf-8')
        else:
            pass
    ip_wsl = std_out_list[0].split(" ")[0]
    if ip_wsl:
        if not ping(ip=ip_wsl):
            pk_print(str_working=rf'''ping {ip_wsl}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            raise
    return ip_wsl
