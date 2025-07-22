import zlib
import yt_dlp
import traceback
import toml
import string
import requests
import datetime
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated

from os.path import dirname
from enum import Enum
from pkg_py.functions_split.get_list_calculated import get_list_calculated


def run_cmd_exe():
    cmd_to_os(cmd=rf"start cmd.exe /k", mode="a")
