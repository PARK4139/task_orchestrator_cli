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

from urllib.parse import urlparse
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.state_via_context import SpeedControlContext
from pathlib import Path
from mutagen.mp3 import MP3
from functools import partial
from fastapi import HTTPException
from enum import Enum
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from collections import Counter
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def set_remote_os_as_nopasswd_v1(**config_remote_os):
    pw = config_remote_os['pw']
    cmd = "sudo grep -n 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers"
    std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
    std_out = get_str_from_list(std_out_list)
    if "nvidia ALL=(ALL:ALL) NOPASSWD:ALL" in std_out:
        ensure_printed("The entry is already present.", 'green')
    else:
        cmd = f"echo '{pw}' | sudo -S bash -c \"echo 'nvidia ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers\""
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
        cmd = f"sudo visudo -c"
        std_out_list, std_err_list = cmd_to_remote_os_with_pw_via_paramiko(cmd=cmd, **config_remote_os)
