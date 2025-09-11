import yt_dlp

import win32con
import uuid
import urllib.parse
import urllib
import tomllib
import time
import threading
import tarfile
import socket
import secrets
import random, math
import pywintypes
import pygetwindow
import platform
import paramiko
import numpy as np
import nest_asyncio
import json
import inspect
import importlib
import hashlib
import datetime
import clipboard
import chardet
import calendar

import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot, Update
from telegram import Bot
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from pynput import mouse

from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern



from sources.functions.does_pnx_exist import is_pnx_existing
import logging
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter


from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_state_via_database import PkSqlite3DB


from sources.objects.pk_local_test_activate import LTA


from pathlib import Path
from passlib.context import CryptContext
from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from fastapi import HTTPException
from datetime import timedelta
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from bs4 import ResultSet

from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.is_d import is_d

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.functions.get_d_working import get_d_working


def get_symmetric_difference_set(set_a, set_b):
    """대칭차집합 A △ B (A 또는 B에만 있는 요소들)"""
    return set(set_a) ^ set(set_b)
