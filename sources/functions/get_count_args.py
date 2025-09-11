import winreg


import win32con
import webbrowser
import uuid
import urllib.parse
import urllib
import undetected_chromedriver as uc
import tqdm
import toml
import toml
import threading
import string
import speech_recognition as sr
import shutil
import secrets
import requests
import random
import pywintypes

import pickle
import paramiko
import pandas as pd
import os, inspect
import os
import keyboard
import importlib
import hashlib
import functools
import datetime
import cv2
import colorama
import calendar
import asyncio
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from typing import TypeVar, List
from tkinter import UNDERLINE
from telegram import Bot, Update
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list



from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened import is_window_opened
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f

from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.pk_map_texts import PkTexts

from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.pk_local_test_activate import LTA

from PIL import Image, ImageFilter
from passlib.context import CryptContext
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from fastapi import HTTPException
from datetime import timedelta
from datetime import datetime, time
from collections import defaultdict, Counter
from base64 import b64decode
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.is_f import is_f
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def get_count_args(func):
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    return func.__code__.co_argcount
