

import win32con
import win32con
import win32com.client
import webbrowser
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tomllib
import toml
import toml
import timeit
import tarfile
import sys
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

import pyaudio
import platform
import pickle
import paramiko
import pandas as pd
import os.path
import os, inspect
import nest_asyncio
import mysql.connector
import mutagen
import math
import keyboard
import json
import ipdb
import inspect
import hashlib
import functools
import datetime
import cv2
import colorama

from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from urllib.parse import quote, urlparse
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
import logging
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext
from PIL import Image
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import timedelta
from datetime import datetime, time
from datetime import datetime
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d

from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def is_target_type_list(target):
    if isinstance(target, list):
        return 1
    else:
        return 0
