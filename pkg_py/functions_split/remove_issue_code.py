import yt_dlp

import win32con
import timeit
import tarfile
import sys
import requests
import random
import pythoncom
import pyautogui
import paramiko
import pandas as pd
import os.path
import os, inspect
import numpy as np
import nest_asyncio
import math
import clipboard
import chardet
import calendar

from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.state_via_database import PkSqlite3DB
from PIL import Image, ImageFilter
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from datetime import datetime
from datetime import date
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_d_working import get_d_working


def remove_issue_code():
    ensure_printed(f'''issu_code is removed {'%%%FOO%%%' if LTA else ''}''')
