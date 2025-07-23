import yt_dlp
# import win32process
# import win32gui
import win32com.client
import webbrowser
import undetected_chromedriver as uc
import traceback
import tqdm
import toml
import timeit
import time
import tarfile
import sys
import string
import socket, time
import secrets
import re
import random
import pywintypes
import pyaudio
import platform
import pickle
import pandas as pd
import hashlib
import cv2
import colorama
import clipboard
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.is_os_windows import is_os_windows

from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def get_extension_set_from_d(dir_path: str) -> set[str]:
    import os
    extensions = set()
    if not os.path.isdir(dir_path):
        return extensions
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            if ext:
                extensions.add(ext)
    return extensions
