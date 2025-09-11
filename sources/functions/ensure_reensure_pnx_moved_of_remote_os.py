import winreg


import win32con
import uuid
import urllib.parse
import urllib
import tqdm
import toml
import toml
import timeit
import threading
import tarfile
import socket
import requests
import re
import random
import pywintypes

import platform
import paramiko
import os.path
import numpy as np
import mysql.connector
import json
import ipdb
import inspect
import hashlib
import functools
import easyocr
import colorama
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front



from sources.functions.get_video_filtered_list import get_video_filtered_list

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.pk_map_texts import PkTexts
from PIL import Image, ImageFilter
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import datetime
from datetime import date
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided

from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def ensure_reensure_pnx_moved_of_remote_os(pnx, **remote_device_target_config):
    std_outs, std_err_list = ensure_command_to_remote_os(cmd=f"rm -rf {pnx}", **remote_device_target_config)
    std_outs, std_err_list = ensure_command_to_remote_os(cmd=f"ls {pnx}", **remote_device_target_config)
    signiture = 'todo'
    for std_out in std_outs:
        if signiture in std_out:
            logging.debug(f'''remove {pnx} at {remote_device_target_config['ip']}  {'%%%FOO%%%' if LTA else ''}''')
        else:
            logging.debug(f'''remove {pnx} at {remote_device_target_config['ip']}  {'%%%FOO%%%' if LTA else ''}''')
            raise
