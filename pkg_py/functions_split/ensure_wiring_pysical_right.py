import zlib

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
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.print_state import print_state
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.directories_reuseable import D_PROJECT

from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA

from paramiko import SSHClient, AutoAddPolicy
from gtts import gTTS
from fastapi import HTTPException
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


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
        ensure_printed(f'''unknown vpc_identifier ({vpc_data.vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''',
                 print_color='red')
        raise
