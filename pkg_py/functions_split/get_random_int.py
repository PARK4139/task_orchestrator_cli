import speech_recognition as sr
import psutil
import nest_asyncio
import ipdb
import hashlib
import asyncio
from urllib.parse import urlparse
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from prompt_toolkit.styles import Style
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_FFMPEG_EXE
from gtts import gTTS
from datetime import timedelta
from cryptography.hazmat.primitives import padding
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux


def get_random_int():
    import secrets
    # ensure_printed(f"{inspect.currentframe().f_code.co_name}()")
    return secrets.randbelow(100)  # 0부터 99까지의 난수 생성
