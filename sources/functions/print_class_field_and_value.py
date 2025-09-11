import zlib
import zipfile
import yt_dlp
import winreg


import undetected_chromedriver as uc
import tomllib
import tomllib
import toml
import threading
import tarfile
import sys
import subprocess, time
import string
import sqlite3
import socket, time
import shutil
import shlex
import secrets
import requests
import re
import random, math

import pythoncom
import pyautogui
import psutil
import platform
import pickle
import paramiko
import pandas as pd
import os.path
import os, inspect
import os
import math
import keyboard
import inspect
import importlib
import hashlib
import easyocr
import datetime
import cv2
import colorama
import colorama
import clipboard
import chardet

import asyncio
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style

from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
import logging
import logging


from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_WORKING
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory

from sources.objects.pk_local_test_activate import LTA


from PIL import Image, ImageFilter
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from datetime import datetime, timedelta
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from sources.functions.get_nx import get_nx

from sources.functions.ensure_value_completed import ensure_value_completed
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def print_class_field_and_value(class_n):  # print 보다는 get 으로 바꾸는게 좋겠다.

    cmd_usage_explanations = []
    cmd_usage_explanations.append(title)
    cmd_usage_explanations.append('\n')
    cmd_usage_explanations.append('<예시> : python console_blurred.py <mode_option>')
    cmd_usage_explanations.append('\n')
    longest_field = max(vars(class_n), key=len)  # mkr_get_longest_field_name
    longest_value = vars(class_n)[longest_field]  # mkr_get_longest_field_value
    for key, value in class_n.__dict__.items():  # mkr_get_field_name_and_field_value
        if not key.startswith('__'):  # 내장 속성 제외
            cmd_usage_explanations.append(f"{key}{" " * (len(longest_field) - len(key))}: {value}")
    cmd_usage_explanations.append('\n')
    for cmd_usage_explanation in cmd_usage_explanations:
        logging.debug(cmd_usage_explanation)
    cmd_usage_explanations.append('\n')
