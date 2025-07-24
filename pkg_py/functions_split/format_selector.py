import zipfile

import win32com.client
import time
import threading
import subprocess, time
import string
import socket, time
import pyglet
import pyautogui
import pyaudio
import ipdb
import colorama
import clipboard
import chardet
from zipfile import BadZipFile
from urllib.parse import quote
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_front import is_window_title_front

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.map_massages import PkMessages2025
from paramiko import SSHClient, AutoAddPolicy
from os import path
from mutagen.mp3 import MP3
from gtts import gTTS
from functools import partial as functools_partial
from Cryptodome.Random import get_random_bytes
from bs4 import ResultSet
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.functions_split.get_d_working import get_d_working


def format_selector(ctx):
    """ 최적의 비디오 및 오디오 형식을 선택하는 함수 """
    formats = ctx.get('formats')
    if not formats:
        raise ValueError("No formats available.")

    # 모든 비디오 포맷 가져오기 (MP4 우선)
    video_formats = sorted(
        [fmt for fmt in formats if fmt.get('vcodec') != 'none'],
        key=lambda fmt: (int(fmt.get('height') or 0), int(fmt.get('vbr') or 0)), reverse=True
    )

    # 모든 오디오 포맷 가져오기
    audio_formats = sorted(
        [fmt for fmt in formats if fmt.get('acodec') != 'none'],
        key=lambda fmt: int(fmt.get('abr') or 0), reverse=True
    )

    # MP4 우선, 없으면 다른 확장자도 허용
    for video in video_formats:
        audio_ext = 'm4a' if video.get('ext') == 'mp4' else video.get('ext')
        compatible_audio = next((audio for audio in audio_formats if audio.get('ext') == audio_ext), None)
        if compatible_audio:
            return {
                'format_id': f"{video['format_id']}+{compatible_audio['format_id']}",
                'ext': video['ext'],
                'requested_formats': [video, compatible_audio],
                'protocol': f"{video.get('protocol', '')}+{compatible_audio.get('protocol', '')}"
            }

    # 아무 형식도 찾지 못한 경우
    raise ValueError("No compatible format found. Check if the video is restricted.")
