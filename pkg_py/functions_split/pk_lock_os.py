import webbrowser
import urllib.parse
import time
import speech_recognition as sr
import socket
import random
import pywintypes
# import pywin32
import mysql.connector
import browser_cookie3
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.directories_reuseable import D_PROJECT

from functools import lru_cache
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.is_d import is_d
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA


def pk_lock_os():
    if is_os_windows():
        save_power_as_s3()
    elif is_os_wsl_linux():
        save_power_as_s3()
    else:
        cmd_to_os('echo TBD')
