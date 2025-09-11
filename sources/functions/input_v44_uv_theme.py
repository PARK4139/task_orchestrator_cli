import zipfile
import winreg


import webbrowser
import urllib
import tqdm
import tomllib
import time
import tarfile
import sqlite3
import speech_recognition as sr
import socket
import secrets
import pywintypes
import pyglet
import pyaudio
import platform
import pickle
import os.path
import math
import functools
import easyocr
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from PySide6.QtWidgets import QApplication



from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
import logging
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.pk_etc import PkFilter


from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_map_texts import PkTexts


from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from fastapi import HTTPException
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
from sources.functions.get_nx import get_nx
from sources.objects.pk_etc import PK_UNDERLINE
from pathlib import Path
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_f import is_f

from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.objects.pk_local_test_activate import LTA
import logging

import logging
from sources.functions.ensure_value_completed import ensure_value_completed


def input_v44_uv_theme(
        str_working: str,
        limit_seconds: int = 30,
        return_default: str | None = None,
        *,
        masked: bool = False,
        fuzzy_accept: list[tuple[str, ...]] | None = None,
        validator=None,
        vi_mode: bool = True,
        **kwargs
):
    """
    input_v44_uv_theme 함수를 ensure_value_completed로 대체
    """
    # fuzzy_accept가 있는 경우 해당 값들을 options에 추가
    options = []
    if fuzzy_accept:
        for group in fuzzy_accept:
            options.extend(group)
    
    # return_default가 있는 경우 options에 추가
    if return_default:
        options.append(return_default)
    
    # validator가 있는 경우 기본값만 반환 (validator는 ensure_value_completed에서 지원하지 않음)
    if validator:
        return return_default
    
    # ensure_value_completed 호출
    return ensure_value_completed(key_hint=str_working, options=options)

