import zipfile
import winreg


import urllib.parse
import urllib
import undetected_chromedriver as uc
import traceback
import toml
import toml
import timeit
import time
import threading
import tarfile
import sys
import subprocess
import string
import socket
import shutil
import re
import random

import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import psutil
import platform
import pickle
import pandas as pd
import os.path
import os, inspect
import os
import numpy as np
import nest_asyncio
import mutagen
import math
import keyboard
import json
import inspect
import hashlib
import datetime
import cv2
import colorama
import colorama
import clipboard
import chardet

import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import quote
from telethon import TelegramClient, events
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.get_list_sorted import get_list_sorted

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.pk_local_test_activate import LTA


from passlib.context import CryptContext
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial
from functools import lru_cache
from datetime import timedelta
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing

import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def ensure_mouse_moved_rel_x(x_rel: float, y_rel: float):
    import inspect
    import pyautogui
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    pyautogui.move(x_rel, y_rel)
