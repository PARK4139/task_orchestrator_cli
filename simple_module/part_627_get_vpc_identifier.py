import keyboard
import ipdb
import importlib
from selenium.webdriver.support.ui import WebDriverWait
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.pk_system_layer_etc import PkFilter

from functools import partial as functools_partial
from collections import Counter
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_vpc_identifier(**config_remote_os):
    vpc_nvidia_serial = get_vpc_nvidia_serial_via_scp(**config_remote_os)
    vpc_identifier_dict = get_vpc_identifier_and_vpc_nvidia_serial_map()
    for nvidia_serial, nick_name in vpc_identifier_dict.items():
        if vpc_nvidia_serial not in nick_name:
            continue
        elif vpc_nvidia_serial in nick_name:
            nvidia_serial = nvidia_serial.replace(PK_BLANK, "_")
            return nvidia_serial
    pk_print(
        working_str=rf'''vpc_identifier not found in {get_vpc_identifier_and_vpc_nvidia_serial_map()} ).  {'%%%FOO%%%' if LTA else ''}''',
        print_color='red')
    raise
