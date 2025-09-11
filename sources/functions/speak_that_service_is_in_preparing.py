import zipfile
import win32com.client
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import threading
import string
import socket, time
import shutil
import requests
import re
import random, math

import pyglet
import paramiko
import pandas as pd
import os.path
import os
import numpy as np
import mutagen
import ipdb
import hashlib
import functools
import easyocr
import colorama
import colorama
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse, parse_qs, unquote
from urllib.parse import urlparse
from typing import TypeVar, List
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern

from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted


from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_context import SpeedControlContext

from PIL import Image
from os import path
from moviepy import VideoFileClip
from functools import lru_cache
from cryptography.hazmat.backends import default_backend
from collections import Counter
from bs4 import ResultSet
from bs4 import BeautifulSoup
from base64 import b64decode
from sources.functions.get_nx import get_nx
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def speak_that_service_is_in_preparing():
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    ensure_spoken_v2(str_working="아직 준비되지 않은 서비스 입니다", comma_delay=0.98)
