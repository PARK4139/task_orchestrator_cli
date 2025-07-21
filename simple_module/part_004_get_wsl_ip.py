

# import pywin32

from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_014_pk_print import pk_print


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
            pk_print(working_str=rf'''ping {ip_wsl}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            raise
    return ip_wsl
