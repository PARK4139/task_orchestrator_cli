import zipfile
import yt_dlp


import win32com.client
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tomllib
import tarfile
import sys
import subprocess
import string
import shlex
import secrets
import requests
import re
import pythoncom
import pyautogui
import pyaudio
import paramiko
import os.path
import os
import mysql.connector
import mutagen
import json
import functools
import easyocr
import datetime
import colorama
import clipboard
import chardet
import calendar

from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from prompt_toolkit import PromptSession

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern


from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.pk_etc import PkFilter


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_context import SpeedControlContext



from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial
from functools import lru_cache
from enum import Enum
from dirsync import sync
from datetime import datetime, timedelta
from datetime import datetime, time
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from collections import Counter
from bs4 import BeautifulSoup
from base64 import b64decode

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def ensure_wsl_flash_directory_flashable (target_device_data):
    if 'no' in target_device_data.device_identifier:
        ensure_command_to_remote_os("mkdir -p ~/Downloads/flash/no_flash/")
    elif 'nx' in target_device_data.device_identifier:
        ensure_command_to_remote_os("mkdir -p ~/Downloads/flash/nx_flash/")
    elif 'xc' in target_device_data.device_identifier:
        ensure_command_to_remote_os("mkdir -p ~/Downloads/flash/xc_flash/")
    elif 'evm' in target_device_data.device_identifier:
        ensure_command_to_remote_os("mkdir -p ~/Downloads/flash/evm_flash/")
    else:
        logging.debug(f'''unknown target_device_data.identifier ({target_device_data.device_identifier}) {'%%%FOO%%%' if LTA else ''}''',
                      print_color='yellow')
        raise
