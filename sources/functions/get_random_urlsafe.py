
import win32con
import win32con
import webbrowser
import urllib.parse
import traceback
import tqdm
import time
import sqlite3
import socket
import re
import os, inspect
import nest_asyncio
import mutagen
import ipdb
import inspect
import datetime
import clipboard
import chardet
import calendar

from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from pytube import Playlist
from prompt_toolkit.styles import Style
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.get_d_working import get_d_working
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_map_texts import PkTexts

from passlib.context import CryptContext
from mysql.connector import connect, Error
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from functools import partial
from colorama import init as pk_colorama_init
from bs4 import ResultSet

from sources.functions.ensure_value_completed import ensure_value_completed

from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging

import logging


def get_random_urlsafe():
    import secrets

    return secrets.token_urlsafe(16)  # 16바이트의 난수를 URL-safe 문자열로 생성
