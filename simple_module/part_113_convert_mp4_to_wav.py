import zipfile
import winreg
import traceback
import tomllib
import timeit
import subprocess
import sqlite3
import requests
import re
import pygetwindow
import pyaudio
import platform
import os.path
import numpy as np
import mysql.connector
import easyocr
from telegram import Bot
from seleniumbase import Driver
from queue import Queue, Empty
from prompt_toolkit import PromptSession
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from os.path import dirname
from enum import Enum
from datetime import datetime, timedelta
from datetime import date
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_014_pk_print import pk_print


def convert_mp4_to_wav(pnx):
    import inspect
    import os

    func_n = inspect.currentframe().f_code.co_name
    '''테스트 필요'''
    pk_print(f'from : {pnx}', print_color='blue')
    file_edited = f'{os.path.splitext(os.path.basename(pnx))[0]}.wav'
    pk_print(f'to   : {file_edited}', print_color='blue')

    path_started = os.getcwd()

    os.system('mkdir storage')
    pk_chdir('storage')
    if os.path.splitext(os.path.basename(pnx))[1] == '.mp4':
        from moviepy import VideoFileClip
        videoclip = VideoFileClip(pnx)
        audioclip = videoclip.audio

        # audioclip.write_audiofile(file_edited, fps= 8000 )
        audioclip.write_audiofile(file_edited, fps=44100)
        audioclip.close()
        videoclip.close()

    pk_chdir(path_started)
