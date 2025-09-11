import toml
import sqlite3
import shutil
import requests
import re
import psutil
import os.path
import json
import ipdb
import importlib
import chardet
from zipfile import BadZipFile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from pynput import mouse

from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_local_test_activate import LTA

from passlib.context import CryptContext
from fastapi import HTTPException
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from collections import Counter
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def check_latest_jetpack_version_and_get_version_seleted(target_device_identifier, jetpack_version):
    return jetpack_version  # code for temp

    target_device_identifier = target_device_identifier.strip()
    target_device_identifier = target_device_identifier.lower()
    if 'no' in target_device_identifier:
        # todo gitlab 에서 latest 파싱하도록 후 target_device_aifw_version 와 비교, 같으면 진행, 다르면 질의(latest 는 몇입니다. 업데이트 할까요?)
        jetpack_version = "5.1.2"
    elif 'nx' in target_device_identifier:
        jetpack_version = "5.0.2"
    elif 'xc' in target_device_identifier:
        jetpack_version = "4.6.5"
    elif 'evm' in target_device_identifier:
        jetpack_version = "4.6.6"
    else:
        logging.debug(f'''unknown target_device_identifier ({target_device_identifier}) {'%%%FOO%%%' if LTA else ''}''')
        raise
    if LTA:
        logging.debug(f'''jetpack_version={jetpack_version} {'%%%FOO%%%' if LTA else ''}''')
    return jetpack_version
