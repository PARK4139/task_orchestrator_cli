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

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI


from sources.objects.pk_local_test_activate import LTA

from paramiko import SSHClient, AutoAddPolicy
from gtts import gTTS
from fastapi import HTTPException
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from base64 import b64encode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
import logging

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def ensure_wiring_pysical_right (target_device_data):
    target_device_identifier = target_device_data.device_identifier

    # bring_NO_flash_kit_from_warehouse()  # zipper bag
    ensure_usb_cable_connected_right()  # HOST_PC 에서 EVM(origin)로 ACCESS      # without_usb_hub
    ensure_lan_cable_connected_right()  # HOST_PC 에서 EVM(origin) LAN6(하단케이스에 적힌) 포트에

    if 'no' in target_device_identifier:

        pass
    elif 'nx' in target_device_identifier:
        pass
    elif 'xc' in target_device_identifier:
        pass
    elif 'evm' in target_device_identifier:
        pass
    else:
        logging.debug(f'''unknown target_device_identifier ({target_device_data.device_identifier}) {'%%%FOO%%%' if LTA else ''}''',
                      print_color='yellow')
        raise
