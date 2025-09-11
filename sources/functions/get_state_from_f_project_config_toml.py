import zipfile
import winreg

            

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

from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern


from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA


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
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided

from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d

from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def get_state_from_f_project_config_toml(pk_state_address):
    if LTA:
        logging.debug(f'''pk_state_address={pk_state_address} {'%%%FOO%%%' if LTA else ''}''')
    pk_toml_address_list = pk_state_address.split('/')
    level_1_dict_n = ""
    level_2_dict_n = ""
    level_3_dict_n = ""
    try:
        level_1_dict_n = pk_toml_address_list[0]
        level_2_dict_n = pk_toml_address_list[1]
        level_3_dict_n = pk_toml_address_list[2]
    except:
        logging.debug(f'''{len(pk_toml_address_list)} is idx limit. {'%%%FOO%%%' if LTA else ''}''')

    level_1_dict = {}
    level_2_dict = {}
    level_3_dict = {}
    # todo
    try:
        level_1_dict = toml.load(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML)[level_1_dict_n]
    except KeyError:
        logging.debug(f'''level_1_dict={level_1_dict}에 해당하는 key 가 없습니다. {'%%%FOO%%%' if LTA else ''}''')
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
