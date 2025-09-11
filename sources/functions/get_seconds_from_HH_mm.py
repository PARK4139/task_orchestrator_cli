import yt_dlp
import winreg



import win32con
import uuid
import urllib
import undetected_chromedriver as uc
import traceback
import tqdm
import toml
import timeit
import time
import threading
import tarfile
import sys
import subprocess, time
import subprocess
import string
import sqlite3
import speech_recognition as sr
import socket
import shutil
import re
import random
import pywintypes


import pythoncom
import pygetwindow
import pyautogui
import pyaudio
import platform
import pickle
import paramiko
import pandas as pd
import os.path
import os
import mysql.connector
import json
import inspect
import importlib
import functools
import datetime
import cv2
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from typing import TypeVar, List
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from pynput import mouse

from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
import logging
import logging

from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted

from sources.functions.ensure_console_cleared import ensure_console_cleared


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.pk_local_test_activate import LTA
from PIL import Image
from os.path import dirname
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial as functools_partial
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime, timedelta
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import BeautifulSoup
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def get_seconds_from_HH_mm(HH, mm):
    import datetime
    now = datetime.datetime.now()
    target_time = datetime.datetime(now.year, now.month, now.day, HH, mm)
    if now > target_time:
        target_time += datetime.timedelta(days=1)
    return (target_time - now).seconds
