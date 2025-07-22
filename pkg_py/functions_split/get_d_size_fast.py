# import win32gui
# import win32gui
import urllib
import traceback
import pandas as pd
import math
import cv2
import asyncio
from pytube import Playlist
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
from mutagen.mp3 import MP3
from gtts import gTTS
from datetime import date
from Cryptodome.Random import get_random_bytes
from base64 import b64decode
from pkg_py.functions_split.get_value_completed import get_value_completed


def get_d_size_fast(path):
    """_d_의 총 크기를 빠르게 계산하는 함수"""
    import os
    total_size = 0
    with os.scandir(path) as it:
        for entry in it:
            try:
                if entry.is_file():
                    total_size += entry.stat().st_size
                elif entry.is_dir():
                    total_size += get_d_size_fast(entry.path)  # 재귀적으로 크기 계산
            except FileNotFoundError:
                pass  # f이 이동 중이거나 삭제된 경우 무시
    return total_size
