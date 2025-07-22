import pygetwindow
import pyaudio
import psutil
import platform
import pandas as pd
import os
import json
import ipdb
import inspect
import easyocr
import browser_cookie3
from urllib.parse import urlparse
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pathlib import Path
from mutagen.mp3 import MP3
from functools import partial
from fastapi import HTTPException
from enum import Enum
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from collections import Counter
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.pk_print import pk_print


def set_remote_os_as_nopasswd_v1(**config_remote_os):
    pw = config_remote_os['pw']
    cmd = "sudo grep -n 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers"
    std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
    std_out = get_str_from_list(std_out_list)
    if "nvidia ALL=(ALL:ALL) NOPASSWD:ALL" in std_out:
        pk_print("The entry is already present.", 'green')
    else:
        cmd = f"echo '{pw}' | sudo -S bash -c \"echo 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers\""
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        cmd = f"sudo visudo -c"
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
