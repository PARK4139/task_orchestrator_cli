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
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from sources.objects.pk_local_test_activate import LTA

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


from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

import logging


def is_containing_number(text):
    import re
    pattern = "[0-9]"
    if re.search(pattern, text):
        return 1
    else:
        return 0
