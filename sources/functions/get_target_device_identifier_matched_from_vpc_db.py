import zlib
import zipfile
import yt_dlp

import webbrowser
import uuid
import urllib.parse
import undetected_chromedriver as uc
import traceback
import tomllib
import timeit
import subprocess, time
import subprocess
import sqlite3
import speech_recognition as sr
import socket, time
import socket
import shutil
import shlex
import secrets
import requests
import random
import pywintypes


import pyglet
import psutil
import os.path
import os, inspect
import os
import numpy as np
import mysql.connector
import mutagen
import math
import json
import importlib
import hashlib
import functools
import easyocr
import datetime
import colorama
import clipboard

import asyncio
from urllib.parse import urlparse
from urllib.parse import quote
from telethon import TelegramClient, events
from telegram import Bot, Update
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from pytube import Playlist
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession

from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front


from sources.functions.get_video_filtered_list import get_video_filtered_list
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.get_d_working import get_d_working
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging
from sources.functions.ensure_printed_once import ensure_printed_once
import logging
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.set_pk_context_state import set_pk_context_state

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER, F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_context import SpeedControlContext

from sources.objects.pk_local_test_activate import LTA

from PIL import Image
from passlib.context import CryptContext
from os.path import dirname
from os import path
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from dirsync import sync
from datetime import datetime, timedelta
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from collections import Counter
from sources.functions.get_nx import get_nx

from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from sources.functions.get_pnxs import get_pnxs
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES

from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def get_target_identifier_matched_from_target_db(vpc_nvidia_serial, target_device_side_mode):
    # todo : target_device_db.sqlite or target_device_db.pickle or target_device_db._toml 에서 가져오도록

    f = F_VPC_MAMNAGEMENT_MAP_TOML
    if target_device_identifier:
        return target_device_identifier
