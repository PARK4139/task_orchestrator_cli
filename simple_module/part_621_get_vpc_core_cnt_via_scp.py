import zipfile
import yt_dlp
import urllib
import undetected_chromedriver as uc
import time
import socket
import shutil
# import pywin32
import pyaudio
import pandas as pd
import mysql.connector
import mutagen
import asyncio
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PySide6.QtWidgets import QApplication
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from os.path import dirname
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def get_vpc_core_cnt_via_scp(vpc_data_raw):
    config_remote_os = {}
    config_remote_os['ip'] = vpc_data_raw.vpc_ip
    config_remote_os['port'] = vpc_data_raw.vpc_port
    config_remote_os['user_n'] = vpc_data_raw.vpc_user_n
    config_remote_os['local_ssh_private_key'] = vpc_data_raw.vpc_local_ssh_private_key
    config_remote_os['local_ssh_public_key'] = vpc_data_raw.vpc_local_ssh_public_key
    std_out_list, std_err_list = cmd_to_remote_os(cmd='ifconfig', **config_remote_os)
