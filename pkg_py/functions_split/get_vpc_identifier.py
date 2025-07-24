import keyboard
import ipdb
import importlib
from selenium.webdriver.support.ui import WebDriverWait
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.system_object.etc import PkFilter

from functools import partial as functools_partial
from collections import Counter
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


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
        str_working=rf'''vpc_identifier not found in {get_vpc_identifier_and_vpc_nvidia_serial_map()} ).  {'%%%FOO%%%' if LTA else ''}''',
        print_color='red')
    raise
