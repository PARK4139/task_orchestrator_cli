
import undetected_chromedriver as uc
import tqdm
import timeit
import time
import shutil
import requests
import pywintypes
import pyglet
import pyaudio
import psutil
import os
import numpy as np
import ipdb
import inspect
import functools
import colorama
import calendar
import asyncio
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from prompt_toolkit import PromptSession
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE

from PIL import Image
from mutagen.mp3 import MP3
from enum import Enum
from datetime import datetime, time
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init

from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style

from sources.objects.pk_local_test_activate import LTA
from sources.functions.get_d_working import get_d_working


def is_aifw_running():
    # ensure_command_to_remote_os(jetpack version)
    todo('%%%FOO%%%')
