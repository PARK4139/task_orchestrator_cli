import zlib
# import win32gui
import win32com.client
import urllib
import tomllib
import toml
import toml
import subprocess
import sqlite3
import shutil
import shlex
import re
# import pywin32
import pyglet
import paramiko
import os.path
import mysql.connector
import math
import json
import ipdb
import inspect
import importlib
import hashlib
import datetime
import colorama
import clipboard
from zipfile import BadZipFile
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from urllib.parse import quote
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from PySide6.QtWidgets import QApplication
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_100_os import is_os_windows, is_os_wsl_linux
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from paramiko import SSHClient, AutoAddPolicy
from gtts import gTTS
from fastapi import HTTPException
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def ensure_wiring_pysical_right(vpc_data):
    vpc_identifier = vpc_data.vpc_identifier

    # bring_NO_flash_kit_from_warehouse()  # zipper bag
    ensure_usb_cable_connected_right()  # HOST_PC 에서 EVM(origin)로 ACCESS      # without_usb_hub
    ensure_lan_cable_connected_right()  # HOST_PC 에서 EVM(origin) LAN6(하단케이스에 적힌) 포트에

    if 'no' in vpc_identifier:

        pass
    elif 'nx' in vpc_identifier:
        pass
    elif 'xc' in vpc_identifier:
        pass
    elif 'evm' in vpc_identifier:
        pass
    else:
        pk_print(f'''unknown vpc_identifier ({vpc_data.vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''',
                 print_color='red')
        raise
