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
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.get_list_calculated import get_list_calculated

from os.path import dirname
from enum import Enum
from pkg_py.functions_split.get_list_calculated import get_list_calculated


def run_cmd_exe():
    ensure_command_excuted_to_os(cmd=rf"start cmd.exe /k", mode="a")
