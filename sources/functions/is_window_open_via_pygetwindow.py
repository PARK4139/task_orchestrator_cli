

import win32com.client
import webbrowser
import urllib.parse
import traceback
import tqdm
import tomllib
import subprocess
import string
import sqlite3
import shutil
import secrets
import random
import pywintypes
import paramiko
import mysql.connector
import ipdb
import clipboard
from zipfile import BadZipFile
from typing import TypeVar, List
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from sources.objects.pk_state_via_context import SpeedControlContext

from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from functools import partial as functools_partial
from functools import partial
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from bs4 import ResultSet
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def is_window_open_via_pygetwindow(window_title):
    import pygetwindow
    windows = pygetwindow.getAllTitles()  # 모든 열린 창들의 제목을 가져옴
    return window_title in windows  # 특정 창이 열려 있는지 확인
