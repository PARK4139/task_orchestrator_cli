import zipfile
import winreg
import urllib
import tqdm
import toml
import tarfile
import sys
import string
import socket
import secrets
import pyglet
import pandas as pd
import os.path
import keyboard
import json
import ipdb
import inspect
import importlib
import datetime
import cv2
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted

from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from pathlib import Path
from passlib.context import CryptContext
from fastapi import HTTPException
from dirsync import sync
from datetime import timedelta
from datetime import datetime, time
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from collections import Counter
from bs4 import ResultSet

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.functions.get_d_working import get_d_working


def merge_pnx_list_via_text_file():
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    f_func_n_txt = rf'{D_TASK_ORCHESTRATOR_CLI}\task_orchestrator_cli_sensitive\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode="f")
    # if not is_window_opened(window_title=f_func_n_txt):
    #     open_pnx(f_func_n_txt, debug_mode=True)
    pnxs = get_list_from_f(f=f_func_n_txt)
    merge_d_list(d_list=pnxs)
