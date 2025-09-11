import zlib
import zipfile
import winreg

import win32con
import uuid
import urllib.parse
import traceback
import tqdm
import toml
import string
import sqlite3
import socket, time
import shlex
import secrets
import requests
import pythoncom
import paramiko
import pandas as pd
import math
import ipdb
import datetime

import asyncio
from zipfile import BadZipFile
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from queue import Queue, Empty
from pynput import mouse
from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
import logging
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext

from functools import lru_cache
from datetime import datetime, time
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from bs4 import ResultSet

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
import logging

from sources.objects.pk_local_test_activate import LTA


def ensure_auto_reboot_test():
    # EVM
    # poweroff
    # disconnect power
    # connect 2pin jumper #EVM의 경우, J#xx 점퍼로 전원인가를 자동화
    # connect power
    pass
