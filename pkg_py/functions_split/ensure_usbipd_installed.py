# import win32gui
# import win32gui
import webbrowser
import uuid
import undetected_chromedriver as uc
import toml
import threading
import tarfile
import subprocess
import secrets
import pywintypes
# import pywin32
import pyautogui
import os.path
import nest_asyncio
import mysql.connector
import mutagen
import hashlib
import easyocr
import clipboard
from urllib.parse import quote, urlparse
from tkinter import UNDERLINE
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_f import is_f
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_windows import is_os_windows

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_usbipd_installed(config_remote_os):
    if is_os_windows():
        if not is_usbipd_installed():
            # explorer https://github.com/dorssel/usbipd-win/releases
            # install usbipd-win_5.0.0_x64.msi
            # usbipd list # APX -> Attached or Shared -> BUSID
            # usbipd bind -b $BUSID
            # usbipd attach --wsl --busid $BUSID --auto-attach
            # wsl -d wsl_ubuntu_24_04_no_flash lsusb # NVIDIA Corp. APX
            cmd_to_remote_os(cmd='sudo apt install -y usbutils',
                             **config_remote_os)  # wsl/wsl_ubuntu_24_04_no_flash/usbutils/lsusb
