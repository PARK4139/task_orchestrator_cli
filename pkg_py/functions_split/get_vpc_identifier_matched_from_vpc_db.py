import zlib
import zipfile
import yt_dlp

import webbrowser
import uuid
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import subprocess, time
import subprocess
import sqlite3
import speech_recognition as sr
import socket, time
import socket
import shutil
import shlex
import secrets
import requests
import random
import pywintypes


import pyglet
import psutil
import os.path
import os, inspect
import os
import numpy as np
import mysql.connector
import mutagen
import math
import json
import importlib
import hashlib
import functools
import easyocr
import datetime
import colorama
import clipboard

import asyncio
from urllib.parse import urlparse
from urllib.parse import quote
from telethon import TelegramClient, events
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
# pk_#
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_CACHE_PRIVATE
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_context import SpeedControlContext

from pkg_py.system_object.local_test_activate import LTA

from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from os import path
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import datetime, timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_CACHE_PRIVATE, D_PKG_PY
from pkg_py.system_object.directories import D_PKG_PY
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs
from pkg_py.functions_split.get_d_working import get_d_working


def get_vpc_identifier_matched_from_vpc_db(vpc_nvidia_serial, vpc_side_mode):
    # todo : vpc_db.sqlite or vpc_db.pickle or vpc_db._toml 에서 가져오도록

    f = F_VPC_MAMNAGEMENT_MAP_TOML
    if vpc_identifier:
        return vpc_identifier
