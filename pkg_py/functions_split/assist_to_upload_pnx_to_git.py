import zipfile
import winreg
# import win32gui
import win32con
import webbrowser
import uuid
import tqdm
import tomllib
import toml
import toml
import timeit
import time
import tarfile
import subprocess
import string
import speech_recognition as sr
import shutil
import requests
import re
import random, math
import random
# import pywin32
# import pywin32
import pyglet
import pyautogui
import psutil
import pickle
import paramiko
import pandas as pd
import nest_asyncio
import mysql.connector
import mutagen
import keyboard
import json
import hashlib
import datetime
import cv2
import colorama
import chardet
import calendar
import asyncio
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from tkinter import UNDERLINE
from telethon import TelegramClient, events
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.pk_system_object.stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.files import F_HISTORICAL_PNX
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.directories import D_PKG_TXT, D_WORKING
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.get_list_calculated import get_list_calculated

from PIL import Image
from pathlib import Path
from gtts import gTTS
from functools import partial as functools_partial
from fastapi import HTTPException
from enum import Enum
from datetime import timedelta
from datetime import datetime, time
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_d_working import get_d_working


def assist_to_upload_pnx_to_git(d_working, git_repo_url, branch_n):
    pk_print(f'''d_working={d_working} {'%%%FOO%%%' if LTA else ''}''')
    loop_cnt = 1
    while 1:
        try:
            if loop_cnt == 1:
                commit_msg = ensure_input_preprocessed(working_str=f"commit_msg=", upper_seconds_limit=60,
                                                       return_default=f"feat: make save point by auto at {get_time_as_('%Y-%m-%d %H:%M')}")
                push_pnx_to_github(d_working=d_working, git_repo_url=git_repo_url, commit_msg=commit_msg,
                                   branch_n=branch_n)
                loop_cnt = loop_cnt + 1
            if not ensure_d_size_stable(d_working, limit_seconds=30):
                if ensure_d_size_stable(d_working, limit_seconds=30):
                    pk_print("📂 change stable after 📂 change detected")
                    commit_msg = ensure_input_preprocessed(working_str=f"commit_msg=", upper_seconds_limit=60,
                                                           return_default=f"feat: make save point by auto at {get_time_as_('%Y-%m-%d %H:%M')}")
                    push_pnx_to_github(d_working=d_working, git_repo_url=git_repo_url, commit_msg=commit_msg,
                                       branch_n=branch_n)
        except:
            import traceback
            pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            break
