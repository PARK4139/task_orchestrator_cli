import zipfile
import winreg
# import win32process
# import win32gui            
# import win32gui
import urllib
import tqdm
import tomllib
import tomllib
import toml
import time
import threading
import sys
import subprocess, time
import subprocess
import sqlite3
import speech_recognition as sr
import socket
import shutil
import shlex
import secrets
import re
import random, math
import random
import pythoncom
import pyglet
import pyaudio
import psutil
import platform
import pickle
import mysql.connector
import math
import keyboard
import json
import ipdb
import easyocr
import cv2
import clipboard
import chardet
import calendar
import asyncio
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from typing import TypeVar, List
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_100_list_logic import get_list_calculated

from PIL import Image, ImageFilter
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def get_state_from_f_pk_config_toml(pk_state_address):
    if LTA:
        pk_print(f'''pk_state_address={pk_state_address} {'%%%FOO%%%' if LTA else ''}''')
    pk_toml_address_list = pk_state_address.split('/')
    level_1_dict_n = ""
    level_2_dict_n = ""
    level_3_dict_n = ""
    try:
        level_1_dict_n = pk_toml_address_list[0]
        level_2_dict_n = pk_toml_address_list[1]
        level_3_dict_n = pk_toml_address_list[2]
    except:
        pk_print(f'''{len(pk_toml_address_list)} is idx limit. {'%%%FOO%%%' if LTA else ''}''')

    level_1_dict = {}
    level_2_dict = {}
    level_3_dict = {}
    # todo
    try:
        level_1_dict = toml.load(F_PK_CONFIG_TOML)[level_1_dict_n]
    except KeyError:
        pk_print(f'''level_1_dict={level_1_dict}에 해당하는 key 가 없습니다. {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return None
    try:
        level_2_dict = level_1_dict[level_2_dict_n]
    except KeyError:
        return None
    if len(pk_toml_address_list) == 2:
        level_2_dict = level_1_dict[level_2_dict_n]
        return level_2_dict
    try:
        level_3_dict = level_2_dict[level_3_dict_n]
    except KeyError:
        return None
    if len(pk_toml_address_list) == 3:
        level_3_dict = level_2_dict[level_3_dict_n]
        return level_3_dict
