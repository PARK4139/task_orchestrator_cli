import uuid
import urllib
import undetected_chromedriver as uc
import tqdm
import tomllib
import toml
import time
import threading
import sqlite3
import speech_recognition as sr
import shutil
import shlex
import secrets
import requests
import re
import pyaudio
import platform
import paramiko
import os.path
import numpy as np
import nest_asyncio
import mysql.connector
import json
import ipdb
import inspect
import importlib
import hashlib
import easyocr
import datetime
import colorama
import colorama
import clipboard
import calendar
import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import quote
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.print_red import print_red
from pkg_py.system_object.performance_logic import pk_measure_seconds, pk_measure_memory
from pkg_py.system_object.is_os_windows import is_os_windows

from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from os import path
from gtts import gTTS
from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from Cryptodome.Cipher import AES
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_token_from_f_txt(f_token, initial_str):
    generate_token_f(f=f_token, initial_str=initial_str)
    token = get_str_from_txt_f(pnx=f_token)
    token = token.replace("\n", "")
    return token
