import zlib
import zipfile
import yt_dlp


import win32con
import uuid
import tqdm
import tomllib
import tomllib
import timeit
import threading
import tarfile
import sys
import subprocess
import string
import sqlite3
import shlex
import secrets
import random, math
import pygetwindow
import psutil
import platform
import math
import json
import ipdb
import inspect
import hashlib
import easyocr
import cv2
import calendar
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_pressed import ensure_pressed

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
# from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image
from pathlib import Path
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from enum import Enum
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from bs4 import ResultSet
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.ensure_printed import ensure_printed


def is_containing_number(text):
    import re
    pattern = "[0-9]"
    if re.search(pattern, text):
        return 1
    else:
        return 0
