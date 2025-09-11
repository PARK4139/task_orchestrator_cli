import zlib
import win32com.client
import uuid
import traceback
import tomllib
import tomllib
import toml
import time
import sys
import socket, time
import shlex
import re
import random, math

import pyaudio
import pickle
import pandas as pd
import numpy as np
import nest_asyncio
import keyboard
import ipdb
import importlib
import functools
import calendar
from urllib.parse import quote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern


from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
import logging

from sources.functions.get_list_sorted import get_list_sorted


from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext

from pathlib import Path
from os import path
from mutagen.mp3 import MP3
from functools import partial as functools_partial
from datetime import datetime
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing


def get_list_included(working_list, include_element):
    pnx_filtered_list = []
    for item in working_list:
        if include_element in item:
            pnx_filtered_list.append(item)
    return pnx_filtered_list
