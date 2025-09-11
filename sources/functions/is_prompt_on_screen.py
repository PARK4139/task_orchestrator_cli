

import win32con
import tarfile
import sqlite3
import socket, time
import re
import random, math
import pywintypes
import pyautogui
import pyaudio
import psutil
import pandas as pd
import os
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import functools
import clipboard
import calendar
import asyncio

from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_d_working import get_d_working
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.encodings import Encoding
from sources.objects.pk_map_texts import PkTexts



from PIL import Image
from functools import partial
from fastapi import HTTPException
from dirsync import sync
from datetime import datetime
from cryptography.hazmat.primitives import padding
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from sources.functions.get_nx import get_nx
from sources.objects.pk_etc import PK_UNDERLINE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_f import is_f
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.does_pnx_exist import is_pnx_existing

import logging


def is_prompt_on_screen(prompt):
    # OCR을 통해 텍스트 추출
    screenshot = get_screenshot()
    extreact_texts = get_extreact_texts_from_image_via_easyocr(screenshot)
    text_extracted = " ".join([r[1] for r in extreact_texts])

    if is_prompt_in_text(prompt=prompt, text=text_extracted):
        return 1
    else:
        return 0
