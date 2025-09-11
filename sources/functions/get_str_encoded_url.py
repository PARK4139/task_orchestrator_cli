import winreg

import win32con
import uuid
import urllib
import undetected_chromedriver as uc
import toml
import sys
import shlex
import pythoncom
import pyaudio
import numpy as np
import nest_asyncio
import ipdb
import inspect
import easyocr
import cv2
import chardet
import calendar
from yt_dlp import YoutubeDL
from urllib.parse import quote
from tkinter import UNDERLINE
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pynput import mouse

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.get_d_working import get_d_working
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING


from PIL import Image
from pathlib import Path
from os import path
from functools import partial as functools_partial
from enum import Enum
from datetime import timedelta
from datetime import datetime
from datetime import date
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from sources.functions.get_nx import get_nx
from sources.functions.get_list_calculated import get_list_calculated

from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def get_str_encoded_url(str_working):
    import urllib
    from urllib.parse import quote
    return urllib.parse.quote(f"{str_working}")
