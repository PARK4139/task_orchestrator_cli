import yt_dlp
import tomllib
import toml
import requests
import re
import pickle
import numpy as np
import inspect
import importlib
import hashlib
import calendar

from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.get_list_sorted import get_list_sorted



from functools import partial
from dirsync import sync
from cryptography.hazmat.backends import default_backend
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style


def is_mic_device_connected():
    import pyaudio
    audio = pyaudio.PyAudio()
    device_count = audio.get_device_count()
    mic_found = False
    for i in range(device_count):
        device_info = audio.get_device_info_by_index(i)
        # 장치가 입력 장치인지 확인
        if device_info.get("maxInputChannels") > 0:
            mic_found = True
            break
    audio.terminate()
    if mic_found:
        return 1
    else:
        return 0
