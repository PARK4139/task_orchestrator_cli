import yt_dlp
import winreg


import win32con
import win32com.client
import uuid
import urllib.parse
import urllib
import traceback
import tqdm
import tomllib
import toml
import toml
import threading
import tarfile
import sys
import subprocess
import string
import sqlite3
import socket
import requests
import re
import random, math
import random
import pyglet
import pygetwindow
import pyaudio
import psutil
import platform
import paramiko
import pandas as pd
import os, inspect
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import math
import keyboard
import json
import ipdb
import inspect
import importlib
import hashlib
import functools
import easyocr
import datetime
import cv2
import colorama
import clipboard
import chardet
import calendar

import asyncio
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import unquote, urlparse, parse_qs
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from queue import Queue, Empty
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical


from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.ensure_command_executed import ensure_command_executed

from sources.functions.set_pk_context_state import set_pk_context_state


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA

from PIL import Image
from pathlib import Path
from paramiko import SSHClient, AutoAddPolicy
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from gtts import gTTS
from functools import partial
from datetime import timedelta
from datetime import datetime, timedelta
from datetime import datetime, time
from datetime import date
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from bs4 import ResultSet
from base64 import b64encode

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE

from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA


def convert_img_to_img_rotated(img_pnx, degree: int):
    import inspect
    import os
    from PIL import Image
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    img_converted = Image.open(img_pnx).rotate(degree)
    img_converted.show()
    img_converted.save(
        f"{os.path.dirname(img_pnx)}   {os.path.splitext(img_pnx)[0]}_$flipped_h{os.path.splitext(img_pnx)[1]}")
