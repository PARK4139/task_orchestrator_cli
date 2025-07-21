import yt_dlp
# import win32process
# import win32gui
# import win32gui
import webbrowser
import uuid
import undetected_chromedriver as uc
import tqdm
import tomllib
import toml
import threading
import sys
import subprocess
import string
import sqlite3
import speech_recognition as sr
import socket, time
import secrets
import re
# import pywin32
# import pywin32
import pyaudio
import pickle
import paramiko
import os, inspect
import numpy as np
import nest_asyncio
import mysql.connector
import mutagen
import ipdb
import hashlib
import colorama
import clipboard
import browser_cookie3
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import quote
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_stamps import STAMP_ATTEMPTED
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.pk_system_layer_files import F_FFMPEG_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from passlib.context import CryptContext
from os.path import dirname
from os import path
from mysql.connector import connect, Error
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial as functools_partial
from functools import partial
from functools import lru_cache
from fastapi import HTTPException
from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from collections import Counter
from base64 import b64decode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.pk_system_layer_directories import D_WORKING, D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_100_Local_test_activate import LTA


def get_vpc_nvidia_serial_via_scp(vpc_data):
    config_remote_os = {}
    config_remote_os['ip'] = vpc_data.vpc_ip
    config_remote_os['port'] = vpc_data.vpc_port
    config_remote_os['user_n'] = vpc_data.vpc_user_n
    config_remote_os['local_ssh_private_key'] = vpc_data.vpc_local_ssh_private_key
    cmd_to_remote_os(cmd='todo', **config_remote_os)
    nvidia_serial = vpc_data.vpc_nvidia_serial
    return nvidia_serial
