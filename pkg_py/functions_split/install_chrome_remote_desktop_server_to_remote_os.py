# import win32gui
import win32con
import win32com.client
import tqdm
import toml
import socket
import shlex
import pywintypes
# import pywin32
import pythoncom
import platform
import os.path
import mutagen
import easyocr
import datetime
import asyncio
from seleniumbase import Driver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from passlib.context import CryptContext
from os import path
from dataclasses import dataclass
from base64 import b64encode
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

from pkg_py.pk_system_object.local_test_activate import LTA


def install_chrome_remote_desktop_server_to_remote_os(users, ip, remote_os_distro_n, wsl_window_title_seg, pw,
                                                      exit_mode):
    # ssh_in_wsl(users=users, ip=ip, remote_os_distro_n=remote_os_distro_n, wsl_window_title_seg=wsl_window_title_seg, pw=pw, exit_mode=exit_mode)
    #
    # # Update package list
    # cmd_to_wsl_os_like_person('sudo apt update')
    #
    # # Install wget
    # cmd_to_wsl_os_like_person('sudo apt install wget')
    #
    # # Download Google Chrome .deb package
    # cmd_to_wsl_os_like_person('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
    #
    # # Install Google Chrome
    # cmd_to_wsl_os_like_person('sudo apt install ./google-chrome-stable_current_amd64.deb')
    pass
