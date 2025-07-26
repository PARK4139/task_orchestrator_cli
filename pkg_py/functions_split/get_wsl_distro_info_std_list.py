import win32con
import sys
import shutil
import shlex
import random
import pygetwindow
import paramiko
import os
import keyboard
import functools
import colorama
import clipboard
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pynput import mouse
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.state_via_context import SpeedControlContext

from mutagen.mp3 import MP3
from base64 import b64decode
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def get_wsl_distro_info_std_list() -> list[str]:
    import subprocess
    try:
        result = subprocess.run(['wsl', '-l', '-v'], capture_output=True)
        output = result.stdout.decode('utf-16')  # ✅
        std_list = output.splitlines()
        highlight_config_dict = {
            "green": [
                'Running'
            ],
            'red': [
                'Stopped'
            ],
        }
        return std_list
    except Exception as e:
        ensure_printed(f"Failed to get WSL details: {e}", print_color='red')
        return []
