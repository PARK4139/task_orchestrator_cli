import zlib
import win32com.client
import urllib.parse
import undetected_chromedriver as uc
import traceback
import timeit
import time
import threading
import string
import sqlite3
import speech_recognition as sr
import requests
import random
import pythoncom
import pyglet
import pygetwindow
import platform
import nest_asyncio
import math
import ipdb
import importlib
import clipboard
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from prompt_toolkit.styles import Style
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pathlib import Path
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from enum import Enum
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux


def convent_bytes_to_str(target: bytes):
    return target.decode('utf-8')
