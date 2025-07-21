import zlib
import yt_dlp
# import win32gui
# import win32gui
import win32con
import win32con
import uuid
import urllib.parse
import traceback
import shlex
import requests
import pythoncom
import pyaudio
import paramiko
import nest_asyncio
import keyboard
import ipdb
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from pynput import mouse
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated
from pathlib import Path
from gtts import gTTS
from functools import partial as functools_partial
from dirsync import sync
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64decode
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_014_pk_print import pk_print


def convert_mkv_to_wav(file_mkv):
    cmd_to_os_like_person_as_admin(rf'ffmpeg -i "{file_mkv}" -ab 160k -ac 2 -ar 44100 -vn {get_pn(file_mkv)}.wav')
