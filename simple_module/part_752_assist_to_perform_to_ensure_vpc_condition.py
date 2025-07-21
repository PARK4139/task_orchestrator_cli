import win32con
import win32com.client
import webbrowser
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import toml
import timeit
import time
import subprocess, time
import sqlite3
import speech_recognition as sr
import socket
import shlex
import pygetwindow
import os.path
import os
import colorama
import calendar
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from pynput import mouse
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from PIL import Image
from passlib.context import CryptContext
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from dirsync import sync
from datetime import date
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def assist_to_perform_to_ensure_vpc_condition():
    # todo:  request_template_raw 를 넣고 request 를 만들고 request 대로 셋팅 수행 ...하는 로직 파이프 고민필요

    import inspect

    func_n = inspect.currentframe().f_code.co_name

    if is_os_windows():
        # mkr_assist_to_perform_to_ensure_vpc_condition
        # todo guide_to_edit_vpc_config_script_and_update_toml        and        save to vpc_mamnagement_map_toml
        # todo : migrate hardcoding to get_from_toml # 현업에서는 협업을 위해서 필요.
        # 고정값은 migrate to toml and get from toml
        # 가변값은 guide
        f = F_VPC_MAMNAGEMENT_MAP_TOML

        # vpc data model orm (OBJECT RELATIONAL MAPPING)
        vpc_data_raw = get_vpc_data_raw_from_vpc_request()
        vpc_data = A2zCarDataStructure.RemoteDeviceDataStructure()
        vpc_data.set_remote_device_data_field_all(pk_structure=vpc_data_raw)
        vpc_data.print_remote_device_data_field_all(instance_name='vpc_data_defined')

        wsl_data_raw = get_wsl_data_raw_data(vpc_data_raw)
        wsl_data = A2zCarDataStructure.RemoteDeviceDataStructure()
        wsl_data.set_remote_device_data_field_all(pk_structure=wsl_data_raw)
        wsl_data.print_remote_device_data_field_all(instance_name='wsl_data')
        # [ how ] msi/wsl_ubuntu_24_04_no_flash/login.
        # msi

        ensure_wsl_distro_installed(wsl_distro_n=wsl_data.vpc_os_distro_n)
        ensure_wsl_distro_session(wsl_distro_n=wsl_data.vpc_os_distro_n)
        ensure_wsl_usb_ip_connection_established(wsl_distro_n=wsl_data.vpc_os_distro_n,
                                                 config_remote_os=config_remote_os)

        if vpc_data.vpc_ip:
            if LTA:
                pk_print(f'''vpc_data.ip={vpc_data.vpc_ip} {'%%%FOO%%%' if LTA else ''}''')
            config_remote_os = {}
            config_remote_os['ip'] = vpc_data.vpc_ip
            config_remote_os['local_ssh_private_key'] = vpc_data.vpc_local_ssh_private_key
            config_remote_os['port'] = vpc_data.vpc_port
            config_remote_os['user_n'] = vpc_data.vpc_user_n

            ensure_ssh_public_key_to_remote_os(**config_remote_os)
            ensure_remote_os_as_nopasswd(**config_remote_os)

        # argument 유효성 검사
        # pk_print(f'''ooo 과 ooo 이 초기화되지 않아 {vpc_identifier} 장비를 베이직 셋업과 스모크 테스트를 진행할 수 없습니다. {'%%%FOO%%%' if LTA else ''}''')
        # pk_print(f'''ooo a2z 외부차량탑재용으로 {vpc_identifier} 장비를 베이직 셋업과 스모크 테스트를 진행하시겠습니까? {'%%%FOO%%%' if LTA else ''}''')
        print_iterable_as_vertical(item_iterable=config_remote_os)
        raise

        ensure_vpc_ready(wsl_data=wsl_data, vpc_data=vpc_data, **config_remote_os)

        assist_to_ensure_vpc_bit(bit_mode='p')

        assist_to_ensure_vpc_bit(bit_mode='c')
