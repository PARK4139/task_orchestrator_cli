import zipfile
import win32com.client
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import threading
import string
import socket, time
import shutil
import requests
import re
import random, math
# import pywin32
import pyglet
import paramiko
import pandas as pd
import os.path
import os
import numpy as np
import mutagen
import ipdb
import hashlib
import functools
import easyocr
import colorama
import colorama
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from typing import TypeVar, List
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.map_massages import PkMessages2025
from pkg_py.pk_system_object.print_red import print_red
from pkg_py.pk_system_object.state_via_context import SpeedControlContext

from PIL import Image
from os import path
from moviepy import VideoFileClip
from functools import lru_cache
from cryptography.hazmat.backends import default_backend
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def speak_that_service_is_in_preparing():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    pk_speak_v2(working_str="아직 준비되지 않은 서비스 입니다", comma_delay=0.98)
