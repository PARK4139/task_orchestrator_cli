import zlib
import zipfile
import winreg


import win32con
import win32com.client
import uuid
import urllib.parse
import tqdm
import tomllib
import toml
import time
import tarfile
import subprocess
import string
import socket, time
import secrets
import re
import random
import pythoncom
import pyglet
import pygetwindow
import pyautogui
import pickle
import paramiko
import json
import ipdb
import inspect
import functools
import datetime
import colorama
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from telethon import TelegramClient, events
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_state_printed import ensure_state_printed
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING



from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from datetime import datetime
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64decode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.objects.pk_local_test_activate import LTA

from sources.functions.get_d_working import get_d_working


def reset_wired_connection_list(wired_connection_no_range, **remote_device_target_config):
    for wired_connection_no in wired_connection_no_range:
        remote_device_target_config['local_ssh_public_key'] = os.path.join(D_USERPROFILE, ".ssh", "id_ed25519.pub") = {'wired_connection_no': wired_connection_no, "address": rf"", "method": "auto",
                                "gateway": "", "dns": ""}
        set_wired_connection(vpc_wired_connection, **remote_device_target_config)
