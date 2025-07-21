

import webbrowser
import undetected_chromedriver as uc
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from mutagen.mp3 import MP3
from functools import partial
from datetime import timedelta
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style


def get_TBD_pnx_working_with_idx_dict(origin_list, minus_list=None, pnx_plus_list=None):
    if pnx_plus_list is not None:
        origin_list = get_list_unioned(list_a=origin_list, list_b=pnx_plus_list)
    if minus_list is not None:
        origin_list = get_list_differenced(list_a=origin_list, list_b=minus_list)
    pnx_working_with_idx_dict = {}
    for index, pnx_working in enumerate(origin_list):
        pnx_working_with_idx_dict[index] = pnx_working
    return pnx_working_with_idx_dict
