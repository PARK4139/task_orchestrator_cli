
import webbrowser
import urllib.parse
import tqdm
import tomllib
import tarfile
import subprocess
import sqlite3
import socket, time
import socket
import random
import pywintypes
import pyglet
import pygetwindow
import pandas as pd
import mutagen
import keyboard
import colorama
import calendar

from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pynput import mouse
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.get_video_filtered_list import get_video_filtered_list
import logging
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.pk_map_texts import PkTexts
from sources.objects.performance_logic import ensure_seconds_measured, pk_measure_memory
from pathlib import Path
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from sources.functions.get_nx import get_nx

from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_f import is_f
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

import logging


def keyDown(key: str):
    import inspect
    import pyautogui
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    pyautogui.keyDown(key)
