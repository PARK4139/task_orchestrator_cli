import zlib
import yt_dlp
import winreg

import win32con
import uuid
import urllib
import undetected_chromedriver as uc
import traceback
import tqdm
import tomllib
import tomllib
import toml
import threading
import sys
import string
import sqlite3
import speech_recognition as sr
import socket
import re
import random, math


import pythoncom
import pyglet
import pygetwindow
import pyaudio
import psutil
import platform
import os.path
import os, inspect
import os
import numpy as np
import nest_asyncio
import mysql.connector
import keyboard
import json
import inspect
import importlib
import hashlib
import functools
import datetime
import clipboard
import chardet
import calendar
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import unquote, urlparse, parse_qs
from typing import TypeVar, List
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA

from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from os import path
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from datetime import datetime, timedelta
from datetime import datetime, time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.objects.pk_etc import PkFilter, PK_UNDERLINE

from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def get_parents_process_pid():
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    cmd = rf'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId'
    lines = ensure_command_executed_like_human_as_admin(cmd=cmd)
    lines = get_list_replaced_element_from_str_to_str(working_list=lines, from_str="\r", to_str="")
    return lines[0]
