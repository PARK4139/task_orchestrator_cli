import zlib

import win32con
import webbrowser
import uuid
import urllib
import tomllib
import toml
import subprocess
import shutil
import secrets
import pywintypes


import pythoncom
import pyglet
import pyautogui
import psutil
import platform
import pandas as pd
import numpy as np
import inspect
import colorama
import asyncio
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot, Update
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from prompt_toolkit import PromptSession
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.get_list_sorted import get_list_sorted

from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI

from PIL import Image, ImageFilter
from PIL import Image
from os.path import dirname
from os import path
from gtts import gTTS
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from dataclasses import dataclass
from collections import defaultdict, Counter
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
import logging

from sources.objects.pk_local_test_activate import LTA
from sources.functions.get_d_working import get_d_working


def get_set_differenced(set_a, set_b):
    return get_difference_set(set_a, set_b)
