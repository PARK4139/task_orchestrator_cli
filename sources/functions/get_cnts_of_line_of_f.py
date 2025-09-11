import zipfile
import yt_dlp

import win32con
import urllib.parse
import tomllib
import toml
import threading
import tarfile
import subprocess
import string
import socket
import shutil
import secrets
import pywintypes
import pygetwindow
import pickle
import nest_asyncio
import mutagen
import inspect
import functools
import easyocr
import colorama
import asyncio
from zipfile import BadZipFile
from urllib.parse import urlparse
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from pytube import Playlist
from pynput import mouse

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_state_via_database import PkSqlite3DB

from PIL import Image
from mysql.connector import connect, Error
from fastapi import HTTPException
from datetime import datetime, timedelta
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from bs4 import BeautifulSoup
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from sources.objects.pk_local_test_activate import LTA
from sources.functions.get_d_working import get_d_working


def get_cnts_of_line_of_f(f):
    with open(file=f, mode='r') as file:
        return sum(1 for line in file)
