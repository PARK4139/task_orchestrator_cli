import zlib
import win32com.client
import urllib.parse
import undetected_chromedriver as uc
import traceback
import timeit
import time
import threading
import string
import sqlite3
import speech_recognition as sr
import requests
import random
import pythoncom
import pyglet
import pygetwindow
import platform
import nest_asyncio
import math
import ipdb
import importlib
import clipboard
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from prompt_toolkit.styles import Style
from sources.functions.get_historical_list import get_historical_list

from sources.functions.get_d_working import get_d_working
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.get_list_sorted import get_list_sorted

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_state_via_context import SpeedControlContext
from pathlib import Path
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from enum import Enum
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64encode
from sources.functions.get_nx import get_nx
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_os_wsl_linux import is_os_wsl_linux


def convent_bytes_to_str(target: bytes):
    return target.decode('utf-8')
