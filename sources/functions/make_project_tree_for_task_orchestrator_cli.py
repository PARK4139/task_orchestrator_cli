import winreg

import win32con
import tomllib
import tomllib
import toml
import speech_recognition as sr
import shutil
import pywintypes
import pyglet
import pygetwindow
import os, inspect
import functools
import colorama
from yt_dlp import YoutubeDL
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from queue import Queue, Empty
from pytube import Playlist

from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted

from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext
from mutagen.mp3 import MP3
from enum import Enum
from datetime import timedelta
from Cryptodome.Random import get_random_bytes
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from pathlib import Path
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.objects.pk_local_test_activate import LTA


def make_project_tree_for_task_orchestrator_cli():
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    leaf_d_list = [
        D_TASK_ORCHESTRATOR_CLI_RESOURCES
    ]
    for item in leaf_d_list:
        ensure_pnx_made(pnx=item, mode="d")
    leaf_files = [
        # ...
    ]
    for item in leaf_files:
        ensure_pnx_made(pnx=item, mode="f")
