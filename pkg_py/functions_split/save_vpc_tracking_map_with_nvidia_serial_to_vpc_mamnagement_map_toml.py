import zlib
import uuid
import toml
import shutil

from seleniumbase import Driver
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.system_object.map_massages import PkMessages2025
from dirsync import sync
from datetime import timedelta
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style


def save_vpc_tracking_map_with_nvidia_serial_to_vpc_mamnagement_map_toml(vpc_data):
    f = F_VPC_MAMNAGEMENT_MAP_TOML

    config_remote_os = vpc_data.config_remote_os
    nvidia_serial = vpc_data.vpc_nvidia_serial

    answer_about_vpc_type = None
    answer_about_side = None
    answer_about_vpc_number = None
    state_to_save = 0
    while 1:
        if state_to_save == 1:
            # todo save
            if answer_about_vpc_number:
                pass
            if answer_about_vpc_type:
                pass
            if answer_about_side:
                pass
            data_to_save_to_toml = {
                f'{nvidia_serial}': f'{answer_about_vpc_type} #{answer_about_vpc_number} {answer_about_side} side',
            }
            # add_data_to_f_toml()
            break
        answer_about_vpc_type = input('no or nx or xc or evm')
        answer_about_vpc_type = answer_about_vpc_type.strip()
        answer_about_vpc_type = answer_about_vpc_type.lower()
        vpc_type = get_vpc_type_conected_via_scp(**config_remote_os)
        if not vpc_type:
            if answer_about_vpc_type == 'no' or answer_about_vpc_type == 'nx':
                answer_about_side = input('a or b?')
                if answer_about_side == 'a' or answer_about_side == 'b':
                    state_to_save = 1
                else:
                    continue
            elif answer_about_vpc_type == 'xc' or answer_about_vpc_type == 'evm':
                state_to_save = 1
                continue
            else:
                # todo red
                continue
