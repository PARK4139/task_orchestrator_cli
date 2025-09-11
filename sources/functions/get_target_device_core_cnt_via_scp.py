import zipfile
import yt_dlp
import urllib
import undetected_chromedriver as uc
import time
import socket
import shutil

# import pyaudio
# import pandas as pd
import mysql.connector
import mutagen
import asyncio
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PySide6.QtWidgets import QApplication
from sources.functions.get_historical_list import get_historical_list

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.encodings import Encoding
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_local_test_activate import LTA
from os.path import dirname
from bs4 import BeautifulSoup
from base64 import b64decode

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.objects.pk_local_test_activate import LTA

from sources.objects.pk_local_test_activate import LTA


def get_target_core_cnt_via_scp (target_device_data_raw):
    remote_device_target_config = {}
    remote_device_target_config['ip'] = target_device_data_raw.target_device_ip
    remote_device_target_config['port'] = target_device_data_raw.target_device_port
    remote_device_target_config['user_n'] = target_device_data_raw.target_device_user_n
    remote_device_target_config['local_ssh_private_key'] = target_device_data_raw.target_device_local_ssh_private_key
    remote_device_target_config['local_ssh_public_key'] = target_device_data_raw.target_device_local_ssh_public_key
    std_outs, std_err_list = ensure_command_to_remote_os(cmd='ifconfig', **remote_device_target_config)
