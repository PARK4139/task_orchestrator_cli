from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_ip_wsl_another_way():
    wsl_ip = None
    std_list = cmd_to_os("wsl ip -4 addr show eth0")
    signiture_str = 'inet '
    for std_str in std_list:
        if signiture_str in std_str:
            wsl_ip = std_str.split('/')[0].split(signiture_str)[1]
            if LTA:
                pk_print(working_str=rf'''wsl_ip="{wsl_ip}" {'%%%FOO%%%' if LTA else ''}''', print_color='green')
    return wsl_ip
