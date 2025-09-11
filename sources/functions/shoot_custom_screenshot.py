import yt_dlp


import urllib
import tomllib
import time
import socket
import shlex

import paramiko
import os
import numpy as np
import importlib
import easyocr
import cv2
import colorama

from zipfile import BadZipFile
from telethon import TelegramClient, events
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from sources.objects.pk_local_test_activate import LTA
from pathlib import Path
from mutagen.mp3 import MP3
from dirsync import sync
from dataclasses import dataclass
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.is_os_wsl_linux import is_os_wsl_linux

from sources.functions.get_d_working import get_d_working


def shoot_custom_screenshot():
    import asyncio
    asyncio.run(shoot_custom_screenshot_via_asyncio())
