
import win32con
import uuid
import traceback
import tqdm
import subprocess, time
import string
import speech_recognition as sr
import shlex
import secrets
import random

import pythoncom
import pyaudio
import nest_asyncio
import math
import ipdb
import hashlib
import datetime
import calendar
from seleniumbase import Driver
from selenium.webdriver.chrome.options import Options
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical

import logging
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.set_pk_context_state import set_pk_context_state

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.pk_local_test_activate import LTA

from passlib.context import CryptContext
from os.path import dirname
from mutagen.mp3 import MP3
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_f import is_f

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.objects.pk_local_test_activate import LTA

import logging
from sources.functions.get_pnxs import get_pnxs


def get_dict_merged(dict_1, dict_2):
    # todo  dict + dict
    pass
