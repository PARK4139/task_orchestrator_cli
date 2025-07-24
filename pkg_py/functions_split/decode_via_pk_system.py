import zlib
import zipfile
import yt_dlp
import winreg

import win32con
import webbrowser
import uuid
import urllib.parse
import urllib
import traceback
import tomllib
import toml
import time
import threading
import sys
import string
import sqlite3
import speech_recognition as sr
import shutil
import random, math
import random
import pywintypes

import pythoncom
import pyglet
import pygetwindow
import psutil
import pickle
import paramiko
import pandas as pd
import os.path
import os
import numpy as np
import nest_asyncio
import mysql.connector
import ipdb
import importlib
import hashlib
import functools
import easyocr
import datetime
import cv2
import colorama
import colorama
import chardet
import calendar

from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import unquote, urlparse, parse_qs
from typing import TypeVar, List
from telethon import TelegramClient, events
from telegram import Bot
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_state import pk_print_state
from pkg_py.functions_split.pk_print_once import pk_print_once

from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_WORKING
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mysql.connector import connect, Error
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from functools import partial
from datetime import timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
from base64 import b64decode
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def decode_via_pk_system(text_encoded):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    text_encoded = text_encoded.replace("2", "8")
    text_encoded = text_encoded.replace("3", "7")
    text_encoded = text_encoded.replace("4", "6")
    text_encoded = text_encoded.replace("6", "4")
    text_encoded = text_encoded.replace("7", "3")
    text_encoded = text_encoded.replace("8", "2")
    return text_encoded
