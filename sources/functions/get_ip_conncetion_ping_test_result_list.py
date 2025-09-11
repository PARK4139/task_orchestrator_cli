

import zipfile
import yt_dlp
import winreg

            

import webbrowser
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tqdm
import tomllib
import tomllib
import toml
import toml
import timeit
import tarfile
import subprocess
import string
import sqlite3
import speech_recognition as sr
import shutil
import shlex
import secrets
import requests
import random, math
import pywintypes
import pyglet
import pygetwindow
import pyautogui
import pickle
import os.path
import os, inspect
import os
import nest_asyncio
import mutagen
import keyboard
import json
import importlib
import functools
import easyocr
import datetime
import cv2
import colorama
import colorama
import clipboard
import chardet
import calendar

import asyncio
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_pressed import ensure_pressed
import logging
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE

from sources.objects.pk_state_via_context import SpeedControlContext



from PIL import Image
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from moviepy import VideoFileClip
from gtts import gTTS
from functools import lru_cache
from enum import Enum
from datetime import datetime, time
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import ResultSet
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.is_d import is_d

from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def get_ip_conncetion_ping_test_result_list():
    ip_allowed_set = get_ip_allowed_set()
    ping_test_result_list = []
    for ip in ip_allowed_set:
        state_success = 0
        state_result = ensure_pinged(ip)
        if state_result is None:
            state_success = 0
        if state_result == 0:
            state_success = 0
        if state_result == 1:
            state_success = 1
        ping_test_result_list.append(("ping", ip, state_success))
        if LTA:
            logging.debug(f'''ping_test_result_list={ping_test_result_list} {'%%%FOO%%%' if LTA else ''}''')
    return ping_test_result_list
