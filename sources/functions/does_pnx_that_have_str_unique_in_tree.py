import zlib


import win32con
import win32con
import win32com.client
import urllib
import traceback
import tqdm
import timeit
import time
import threading
import tarfile
import subprocess, time
import subprocess
import secrets
import re
import random
import pywintypes

import pythoncom
import pyglet
import pyautogui
import psutil
import platform
import pickle
import paramiko
import os.path
import mutagen
import hashlib
import easyocr
import cv2
import colorama

import asyncio
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_d_working import get_d_working
from sources.functions.ensure_pressed import ensure_pressed
import logging
import logging

from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts

from PIL import Image
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime, time
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64encode

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

import logging
from sources.functions.get_pnxs import get_pnxs


def does_pnx_that_have_str_unique_in_tree(str_unique, str_positive, tree_pnx=None):
    import os

    if tree_pnx is None:
        f_list = os.listdir()
    else:
        f_list = []
        for root, d_nx_list, f_nx_list in os.walk(tree_pnx):
            for f_nx in f_nx_list:
                item_pnx = os.path.abspath(os.path.join(root, f_nx))
                f_list.append(item_pnx)

    for f in f_list:
        if is_pattern_in_prompt(f, str_unique):
            logging.debug(str_positive)
            return 1
    else:
        return 0
