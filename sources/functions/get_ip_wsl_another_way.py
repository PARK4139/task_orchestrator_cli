from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.pk_local_test_activate import LTA
import logging

from sources.objects.pk_local_test_activate import LTA
from sources.functions.ensure_command_executed import ensure_command_executed
import logging


def get_ip_wsl_another_way():
    wsl_ip = None
    std_list = ensure_command_executed("wsl ip -4 addr show eth0")
    signiture_str = 'inet '
    for std_str in std_list:
        if signiture_str in std_str:
            wsl_ip = std_str.split('/')[0].split(signiture_str)[1]
            if LTA:
                logging.debug(rf'''wsl_ip="{wsl_ip}" {'%%%FOO%%%' if LTA else ''}''')
    return wsl_ip
