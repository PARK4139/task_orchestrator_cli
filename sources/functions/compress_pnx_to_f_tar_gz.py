

import winreg

import win32con
import webbrowser
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import time
import tarfile
import subprocess, time
import subprocess
import string
import sqlite3
import speech_recognition as sr
import socket
import shlex
import secrets
import requests
import re
import random
import pywintypes

import pythoncom
# import pyaudio
# import pandas as pd
import os.path
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import json
import ipdb
import hashlib
import functools
import easyocr
import datetime
import cv2
import chardet
import calendar
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from queue import Queue, Empty
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory

from sources.objects.pk_local_test_activate import LTA


from PIL import Image, ImageFont, ImageDraw
from PIL import Image
from pathlib import Path
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import lru_cache
from fastapi import HTTPException
from dirsync import sync
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64encode
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_d import is_d
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
import logging

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def compress_pnx_to_f_tar_gz(pnx, dst):
    import tarfile
    import os

    pnx = get_pnx_windows_style(pnx)
    dst = get_pnx_windows_style(dst)

    # Ensure the source exists
    if not os.path.exists(pnx):
        raise FileNotFoundError(f"Source path '{pnx}' does not exist.")

    # Create a tar.gz archive
    with tarfile.open(dst, "w:gz") as tar:
        def preserve_metadata(tarinfo):
            """
            Preserve file metadata (permissions, ownership, timestamps).
            """
            tarinfo.preserve = True  # Ensure extended metadata is kept
            return tarinfo

        # Add the source directory, preserving metadata
        tar.add(pnx, arcname=os.path.basename(pnx), recursive=True, filter=preserve_metadata)
