import zipfile
import winreg

import uuid
import urllib.parse
import traceback
import toml
import timeit
import time
import threading
import tarfile
import subprocess
import socket, time
import socket
import shutil
import re
import pywintypes
import pythoncom
import pyglet
import pyaudio
import psutil
import pandas as pd
import os, inspect
import numpy as np
import nest_asyncio
import ipdb
import importlib
import easyocr
import colorama
import colorama

import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import quote
from telegram import Bot, Update
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory
from pkg_py.system_object.get_list_calculated import get_list_calculated
from PIL import Image, ImageFilter
from pathlib import Path
from mutagen.mp3 import MP3
from gtts import gTTS
from fastapi import HTTPException
from enum import Enum
from datetime import datetime, timedelta
from datetime import datetime
from dataclasses import dataclass
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from base64 import b64encode
from base64 import b64decode
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_pnxs import get_pnxs


def report_vpc_test_report(issue_code, solution_code):
    # issue discovered
    pass
