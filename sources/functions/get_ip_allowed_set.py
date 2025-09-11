

import zlib

import traceback
import tomllib
import timeit
import time
import tarfile
import sys
import speech_recognition as sr
import socket
import random
import pythoncom
import pyaudio
import numpy as np
import keyboard
import json
import inspect
import importlib
import colorama
import clipboard
import asyncio
from zipfile import BadZipFile
from pynput import mouse
from prompt_toolkit.styles import Style

from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from os.path import dirname
from functools import partial as functools_partial
from functools import partial
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from sources.objects.pk_etc import PkFilter, PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.get_pnx_windows_style import get_pnx_windows_style


def get_ip_allowed_set():
    ip_allowed_set = [
        get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_acu_it.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_a_side.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_b_side.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_test_02114.toml', initial_str=""),  # msi
        get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_test_10114.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_test_02124.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_target_test_10124.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/pk_token_ip_galaxy_book_02076.toml', initial_str=""),
        'localhost',
        '10.10.10.114',
        '119.207.161.135',
    ]
    return ip_allowed_set
