import zipfile


import urllib
import undetected_chromedriver as uc
import tqdm
import tomllib
import toml
import timeit
import threading
import sys
import secrets
import requests
import random, math
import pywintypes

import pythoncom
import pyglet
import pyautogui
import psutil
import pickle
import paramiko
import os
import mutagen
import inspect
import hashlib
import easyocr
import datetime
import cv2
import clipboard
import calendar

from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from typing import TypeVar, List
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
import logging
import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA

from os import path
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from enum import Enum
from datetime import datetime, time
from datetime import datetime
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

import logging
from sources.functions.get_d_working import get_d_working


def convert_mp4_to_webm(src):
    import inspect
    import os

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    '''테스트 필요'''

    logging.debug(f'from : {src}')
    file_edited = f'{os.path.splitext(os.path.basename(src))[0]}.webm'
    logging.debug(f'to   : {file_edited}')

    path_started = os.getcwd()
    os.system("chcp 65001 >NUL")
    os.system('mkdir storage >NUL')
    os.chdir('storage')
    os.system(f'"{F_FFMPEG_EXE}" -i "{src}" -f webm -c:v libvpx -b:v 1M -acodec libvorbis "{file_edited}" -hide_banner')
    os.chdir(path_started)
