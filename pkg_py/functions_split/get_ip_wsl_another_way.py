from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed


def get_ip_wsl_another_way():
    wsl_ip = None
    std_list = ensure_command_excuted_to_os("wsl ip -4 addr show eth0")
    signiture_str = 'inet '
    for std_str in std_list:
        if signiture_str in std_str:
            wsl_ip = std_str.split('/')[0].split(signiture_str)[1]
            if LTA:
                ensure_printed(str_working=rf'''wsl_ip="{wsl_ip}" {'%%%FOO%%%' if LTA else ''}''', print_color='green')
    return wsl_ip
