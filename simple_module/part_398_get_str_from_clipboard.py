import winreg
import webbrowser
import tomllib
import tomllib
import toml
import toml
import shutil
# import pywin32
import psutil
import platform
import pickle
import nest_asyncio
import ipdb
import colorama
import calendar
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from prompt_toolkit.styles import Style
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE

from PIL import Image
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from functools import partial as functools_partial
from enum import Enum
from dirsync import sync
from datetime import date
from bs4 import BeautifulSoup
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style


def get_str_from_clipboard():
    # Get-Clipboard  # 클립보드 내용 확인
    return pk_paste()
