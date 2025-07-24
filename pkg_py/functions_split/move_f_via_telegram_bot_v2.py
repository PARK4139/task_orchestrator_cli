import win32com.client
import undetected_chromedriver as uc
import tomllib
import toml
import time
import threading
import sys
import speech_recognition as sr
import socket
import shlex
import secrets
import random
import pywintypes
import pyglet
import pygetwindow
import pyautogui
import paramiko
import pandas as pd
import mysql.connector
import keyboard
import json
import datetime
import cv2
import browser_cookie3
import asyncio
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pynput import mouse
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.system_object.directories import D_PKG_TXT, D_WORKING
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.state_via_context import SpeedControlContext
from PIL import Image
from pathlib import Path
from os.path import dirname
from mutagen.mp3 import MP3
from fastapi import HTTPException
from datetime import datetime
from datetime import date
from collections import Counter
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.get_d_working import get_d_working


def move_f_via_telegram_bot_v2(f):
    from telegram import Bot

    token_telegram = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_telegram.txt', initial_str="")
    token_telegram_chat_id = get_token_from_f_token(f_token=rf'{D_PKG_TXT}\token_telegram_chat_id.txt', initial_str="")
    bot = Bot(token=token_telegram)

    async def move_f_to_telegram_bot_chat_room():
        try:
            with open(f, "rb") as f_obj:
                await bot.send_document(chat_id=token_telegram_chat_id, document=f_obj, timeout=60)  # 기본 20초에서 60초로 증가
            print("_f_ 전송 성공!")
        except Exception as e:
            print(f"❌ 오류 발생: {e}")

    import asyncio
    asyncio.run(move_f_to_telegram_bot_chat_room())
