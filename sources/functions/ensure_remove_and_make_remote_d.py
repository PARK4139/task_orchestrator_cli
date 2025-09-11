import winreg

import urllib
import traceback
import tqdm
import toml
import subprocess
import shlex
import requests
import random, math
import random
import pywintypes
import pythoncom
import pygetwindow
import pyautogui
# import pyaudio
# import pandas as pd
import os
import numpy as np
import nest_asyncio
import mysql.connector
import inspect
import importlib
import hashlib
import easyocr
import cv2
from urllib.parse import urlparse
from urllib.parse import quote
from telegram import Bot, Update
from selenium.webdriver.support import expected_conditions as EC
from pynput import mouse
from prompt_toolkit import PromptSession
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.pk_etc import PkFilter

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from sources.objects.pk_state_via_context import SpeedControlContext
from pathlib import Path
from paramiko import SSHClient, AutoAddPolicy
from moviepy import VideoFileClip
from dirsync import sync
from datetime import timedelta
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from bs4 import ResultSet
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_list_calculated import get_list_calculated

from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_d_working import get_d_working


def ensure_remove_and_make_remote_d(d, remote_device_target_config):
    # remove d
    ensure_reensure_pnx_moved_of_remote_os(d=d, **remote_device_target_config)

    # make d
    std_outs, std_err_list = ensure_command_to_remote_os(d=f"mkdir -p {d}", **remote_device_target_config)
    for std_out in std_outs:
        logging.debug(rf'''std_out={std_out}  {'%%%FOO%%%' if LTA else ''}''')
        raise
