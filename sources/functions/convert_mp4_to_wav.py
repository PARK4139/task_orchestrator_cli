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

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB
from os.path import dirname
from enum import Enum
from datetime import datetime, timedelta
from datetime import date
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from sources.functions.get_nx import get_nx

from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing

import logging


def convert_mp4_to_wav(pnx):
    import inspect
    import os

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    '''테스트 필요'''
    logging.debug(f'from : {pnx}')
    file_edited = f'{os.path.splitext(os.path.basename(pnx))[0]}.wav'
    logging.debug(f'to   : {file_edited}')

    path_started = os.getcwd()

    os.system('mkdir storage')
    os.chdir('storage')
    if os.path.splitext(os.path.basename(pnx))[1] == '.mp4':
        from moviepy import VideoFileClip
        videoclip = VideoFileClip(pnx)
        audioclip = videoclip.audio

        # audioclip.write_audiofile(file_edited, fps= 8000 )
        audioclip.write_audiofile(file_edited, fps=44100)
        audioclip.close()
        videoclip.close()

    os.chdir(path_started)
