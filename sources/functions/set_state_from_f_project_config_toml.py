import zlib
import yt_dlp

import win32con
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import toml
import threading
import tarfile
import sys
import subprocess, time
import string


import pythoncom
import pygetwindow
import pyautogui
# import pyaudio
# import pandas as pd
import os
import nest_asyncio
import mysql.connector
import mutagen
import math
import keyboard
import easyocr
import clipboard
from zipfile import BadZipFile
from urllib.parse import urlparse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern


from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_state_printed import ensure_state_printed
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts



from passlib.context import CryptContext
from functools import partial
from enum import Enum
from cryptography.hazmat.primitives import padding
from pathlib import Path
from sources.functions.get_list_calculated import get_list_calculated

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.objects.pk_local_test_activate import LTA

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def set_state_from_f_project_config_toml(pk_state_address, pk_state_value):
    pk_toml_address_list = pk_state_address.split('/')
    if LTA:
        logging.debug(f'''pk_state_address={pk_state_address} {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''pk_state_value={pk_state_value} {'%%%FOO%%%' if LTA else ''}''')
    level_1_dict_n = ""
    level_2_dict_n = ""
    level_3_dict_n = ""
    try:
        level_1_dict_n = pk_toml_address_list[0]
        level_2_dict_n = pk_toml_address_list[1]
        level_3_dict_n = pk_toml_address_list[2]
    except:
        if LTA:
            logging.debug(f'''{len(pk_toml_address_list)} is idx limit. in setter {'%%%FOO%%%' if LTA else ''}''')

    level_1_dict = {}
    level_2_dict = {}
    level_3_dict = {}
    try:
        level_1_dict = toml.load(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML)[level_1_dict_n]
    except KeyError:
        logging.debug(f'''level_1_dict={level_1_dict}에 해당하는 key 가 없어 생성합니다. {'%%%FOO%%%' if LTA else ''}''')
        level_1_dict = toml.load(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML)[level_1_dict]
        with open(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML, "w") as f:
            toml.dump(level_1_dict, f)
    try:
        level_2_dict = level_1_dict[level_2_dict_n]
    except KeyError:
        logging.debug(f'''level_2_dict_n={level_2_dict_n}에 해당하는 key 가 없어 생성합니다. {'%%%FOO%%%' if LTA else ''}''')
        level_1_dict[level_2_dict_n] = pk_state_value
        with open(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML, "w") as f:
            toml.dump(level_1_dict, f)
    if len(pk_toml_address_list) == 2:
        level_1_dict[level_2_dict_n] = pk_state_value
        with open(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML, "w") as f:
            toml.dump(level_1_dict, f)
    try:
        level_3_dict = level_2_dict[level_3_dict_n]
    except KeyError:
        logging.debug(f'''level_3_dict_n={level_3_dict_n}에 해당하는 key 가 없어 생성합니다. {'%%%FOO%%%' if LTA else ''}''')
        level_2_dict[level_3_dict_n] = pk_state_value
        with open(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML, "w") as f:
            toml.dump(level_2_dict, f)
    if len(pk_toml_address_list) == 3:
        level_2_dict[level_3_dict_n] = pk_state_value
        with open(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML, "w") as f:
            toml.dump(level_2_dict, f)
