import yt_dlp
import winreg

import win32com.client
import urllib
import undetected_chromedriver as uc
import tqdm
import tomllib
import toml
import timeit
import tarfile
import sys
import speech_recognition as sr
import socket
import shlex
import re
import pywintypes

import pythoncom
import pygetwindow
import pyaudio
import os.path
import os
import numpy as np
import mysql.connector
import mutagen
import math
import keyboard
import inspect
import importlib
import hashlib
import cv2
import colorama
import colorama
import calendar

import asyncio
from zipfile import BadZipFile
from urllib.parse import urlparse
from urllib.parse import quote, urlparse
from urllib.parse import quote
from typing import TypeVar, List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB

from sources.objects.pk_local_test_activate import LTA

from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def make_matrix_console():
    import inspect
    import os
    import subprocess

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    os.system('color 0A')
    os.system('color 02')
    while 1:
        lines = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8').split("\n")
        for line in lines:
            if "" != line:
                if os.getcwd() != line:
                    logging.debug(lines)
        ensure_slept(seconds=60)
