
# from base64 import b64decode
# from base64 import b64encode
# from bs4 import BeautifulSoup
# from bs4 import ResultSet
# from collections import Counter
# from collections import defaultdict
# from collections import defaultdict, Counter
# from colorama import Fore
# from colorama import init as pk_colorama_init
# from concurrent.futures import ThreadPoolExecutor
# from Cryptodome.Cipher import AES
# from Cryptodome.Random import get_random_bytes
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import padding
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from dataclasses import dataclass
# from datetime import date
# from datetime import datetime
# from datetime import datetime, time
# from datetime import datetime, timedelta
# from datetime import timedelta
# from dirsync import sync
# from enum import Enum
# from fastapi import HTTPException
# from functools import lru_cache
# from functools import partial
# from functools import partial as functools_partial
# from functools import wraps
# from glob import glob
# from gtts import gTTS
# from moviepy import VideoFileClip
# from mutagen.mp3 import MP3
# from mysql.connector import connect, Error
# from os import environ
# from os import path
# from os.path import dirname
# from paramiko import SSHClient, AutoAddPolicy
# from passlib.context import CryptContext
# from pathlib import Path
# from PIL import Image
# from PIL import Image, ImageFilter
# from PIL import Image, ImageFont, ImageDraw
# from PIL import Image, ImageFont, ImageDraw, ImageFilter
# from pkg_py.functions_split.ensure_printed import ensure_printed
# from pkg_ps1.system_object.process import ensure_process_killed_by_window_title_seg
# from pkg_py.functions_split import ensure_pycharm_module_optimize
# from pkg_py.functions_split import ensure_keyboard_mouse_macro
# from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
# from pkg_py.functions_split.backup_workspace import backup_workspace
# from pkg_py.functions_split.check_min_non_null_or_warn import check_min_non_null_or_warn
# from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
# from pkg_py.functions_split.ensure_copied_and_pasted_with_keeping_clipboard import ensure_copied_and_pasted_with_keeping_clipboard
# from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
# from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
# from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
# from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
# from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
# from pkg_py.functions_split.ensure_elapsed_time_logged import ensure_elapsed_time_logged
# from pkg_py.functions_split.ensure_func_info_loaded import ensure_func_info_loaded
# from pkg_py.functions_split.ensure_func_info_saved import ensure_func_info_saved
# from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
# from pkg_py.functions_split.ensure_pk_system_started_v5 import ensure_pk_system_started_v5
# from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
# from pkg_py.functions_split.ensure_start_time_logged import ensure_start_time_logged
# from pkg_py.functions_split.ensure_tmux_pk_session_removed import ensure_tmux_pk_session_removed
# from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
# from pkg_py.functions_split.ensure_window_to_front_core import ensure_window_to_front_core
# from pkg_py.functions_split.ensure_window_to_front_v2 import ensure_window_to_front_v2
# from pkg_py.functions_split.ensure_windows_closed import ensure_windows_closed
# from pkg_py.functions_split.get_cmd_to_autorun import get_cmd_to_autorun
# from pkg_py.functions_split.get_d_working import get_d_working
# from pkg_py.functions_split.get_f_historical import get_f_historical
# from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
# from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
# from pkg_py.functions_split.get_file_id import get_file_id
# from pkg_py.functions_split.get_front_window_title import get_front_window_title
# from pkg_py.functions_split.get_historical_list import get_historical_list
# from pkg_py.functions_split.get_idx_list import get_idx_list
# from pkg_py.functions_split.get_list_by_file_id import get_list_by_file_id
# from pkg_py.functions_split.get_list_calculated import get_list_calculated
# from pkg_py.functions_split.get_list_deduplicated import get_list_deduplicated
# from pkg_py.functions_split.get_list_from_f import get_list_from_f
# from pkg_py.functions_split.get_list_removed_empty import get_list_removed_empty
# from pkg_py.functions_split.get_list_removed_none import get_list_removed_none
# from pkg_py.functions_split.get_list_sorted import get_list_sorted
# from pkg_py.functions_split.get_list_striped import get_list_striped
# from pkg_py.functions_split.get_list_striped_element import get_list_striped_element
# from pkg_py.functions_split.get_list_without_none import get_list_without_none
# from pkg_py.functions_split.get_nx import get_nx
# from pkg_py.functions_split.get_os_n import get_os_n
# from pkg_py.functions_split.get_p import get_p
# from pkg_py.functions_split.get_pk_program_language_v2 import get_pk_program_language_v2
# from pkg_py.functions_split.get_pk_system_process_pnxs import get_pk_system_process_pnxs
# from pkg_py.functions_split.get_pk_wsl_mount_d import get_pk_wsl_mount_d
# from pkg_py.functions_split.get_pk_wsl_mount_d_v1 import get_pk_wsl_mount_d_v1
# from pkg_py.functions_split.get_pnxs import get_pnxs
# from pkg_py.functions_split.get_pnxs_from_d_working import get_pnxs_from_d_working
# from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
# from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
# from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
# from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
# from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_processes
# from pkg_py.functions_split.get_str_from_f import get_str_from_f
# from pkg_py.functions_split.get_time_as_ import get_time_as_
# from pkg_py.functions_split.get_time_as_v1 import get_time_as_v1
# from pkg_py.functions_split.get_txt_highlighted import get_txt_highlighted
# from pkg_py.functions_split.get_unique_filename import get_unique_filename
# from pkg_py.functions_split.get_value_by_file_id import get_value_by_file_id
# from pkg_py.functions_split.get_value_completed import get_value_completed
# from pkg_py.functions_split.get_value_completed_v3 import get_value_completed_v3
# from pkg_py.functions_split.get_values_from_historical_database_routine import get_values_from_historical_database_routine
# from pkg_py.functions_split.get_values_from_historical_database_routine_v2 import get_values_from_historical_database_routine_v2
# from pkg_py.functions_split.get_values_from_historical_file import get_values_from_historical_file
# from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
# from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
# from pkg_py.functions_split.get_video_filtered_list_v4 import get_video_filtered_list_v4
# from pkg_py.functions_split.get_webdriver_options_customed import get_webdriver_options_customed
# from pkg_py.functions_split.get_weekday_as_korean import get_weekday_as_korean
# from pkg_py.gui_util import get_windows_opened
# from pkg_py.functions_split.get_windows_opened_via_win32gui import get_windows_opened_via_win32gui
# from pkg_py.functions_split.get_x import get_x
# from pkg_py.functions_split.guide_pk_error_mssage import guide_pk_error_mssage
# from pkg_py.functions_split.guide_to_use_pk_system_process import guide_to_use_pk_system_process
# from pkg_py.functions_split.is_d import is_d
# from pkg_py.functions_split.is_f import is_f
# from pkg_py.functions_split.is_internet_connected import is_internet_connected
# from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
# from pkg_py.functions_split.is_losslesscut_running_v1 import is_losslesscut_running_v1
# from pkg_py.functions_split.is_os_windows import is_os_windows
# from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
# from pkg_py.functions_split.is_path_like import is_path_like
# from pkg_py.functions_split.is_url import is_url
# from pkg_py.functions_split.is_window_opened import is_window_opened
# from pkg_py.functions_split.is_window_title_front import is_window_title_front
# from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
# from pkg_py.functions_split.kill_losslesscut import kill_losslesscut
# from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
# from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
# from pkg_py.functions_split.load_logged_set import load_logged_set
# from pkg_py.functions_split.move_window_to_front_via_pid import move_window_to_front_via_pid
# from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
# from pkg_py.functions_split.ensure_all_import_script_printed import ensure_modules_printed
# from pkg_py.functions_split.ensure_functions_splited import ensure_functions_splited
# from pkg_py.functions_split.ensure_functions_splited_v2 import ensure_functions_splited_v2
# from pkg_py.functions_split.ensure_loop_delayed_at_loop_foot import ensure_loop_delayed_at_loop_foot
# from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config
# from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
# from pkg_py.functions_split.ensure_pressed import ensure_pressed
# from pkg_py.functions_split.ensure_pressed_v2 import ensure_pressed_v2
# from pkg_py.functions_split.ensure_printed import ensure_printed
# from pkg_py.functions_split.print_once import print_once
# from pkg_py.functions_split.ensure_state_printed import ensure_state_printed
# from pkg_py.functions_split.replace_f_nx_list_from_old_str_to_new_str import replace_f_nx_list_from_old_str_to_new_str
# from pkg_py.functions_split.ensure_slept import ensure_slept
# from pkg_py.functions_split.sleep_v2 import sleep_v2
# 
# from pkg_py.functions_split.ensure_spoken import ensure_spoken
# from pkg_py.functions_split.ensure_spoken_v2 import ensure_spoken_v2
# from pkg_py.functions_split.ensure_typed import ensure_typed
# from pkg_py.functions_split.ensure_typed_v2 import ensure_typed_v2
# from pkg_py.functions_split.print_and_save_log_to_file import print_and_save_log_to_file
# from pkg_py.functions_split.print_green import print_green
# from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
# from pkg_py.functions_split.print_light_black import print_light_black
# from pkg_py.functions_split.print_light_blue import print_light_blue
# from pkg_py.functions_split.print_light_white import print_light_white
# from pkg_py.functions_split.print_magenta import print_magenta
# from pkg_py.functions_split.print_pk_ls import print_pk_ls
# from pkg_py.functions_split.print_pk_ls_v4 import print_pk_ls_v4
# from pkg_py.functions_split.print_pk_ver import print_pk_ver
# from pkg_py.functions_split.print_prompt_via_colorama import print_prompt_via_colorama
# from pkg_py.functions_split.print_red import print_red
# from pkg_py.functions_split.print_yellow import print_yellow
# from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
# from pkg_py.functions_split.restore_workspace_from_latest_archive import restore_workspace_from_latest_archive
# from pkg_py.functions_split.ensure_losslesscut_ran import ensure_losslesscut_ran
# from pkg_py.functions_split.run_pk_system_process_by_path import run_pk_system_process_by_path
# from pkg_py.functions_split.sanitize_filename import sanitize_filename
# from pkg_py.functions_split.save_logged_set import save_logged_set
# from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
# from pkg_py.functions_split.set_values_to_historical_file import set_values_to_historical_file
# from pkg_py.functions_split.split_by_top_level_def import split_by_top_level_def
# from pkg_py.functions_split.switch_to_keyboard_mode_to_english_at_windows import switch_to_keyboard_mode_to_english_at_windows
# from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
# from pkg_py.functions_split.ensure_str_writen_to_f import ensure_str_writen_to_f
# from pkg_py.pk_colorful_cli_util import print, ensure_printed, ensure_printed, ensure_printed, ensure_printed, print_magenta, print_light_white, ColoramaUtil, print_ment_via_colorama, print_success, prijnt_as_log, print_yellow
# from pkg_py.pk_core_constants import USERPROFILE, HOSTNAME, UNDERLINE, BLANK, BIGGEST_PNXS, SMALLEST_PNXS, PLAYING_SOUNDS, COUNTS_FOR_GUIDE_TO_SLEEP,VIDEO_IDS_ALLOWED, AUDIO_IDS_ALLOWED, STORAGE_VIDEOES_MERGED, PROJECT_PARENTS_D, DESKTOP, DOWNLOADS, PKG_IMAGE, PKG_DPL, PKG_TXT
# from pkg_py.gui_util import GuiUtil, get_display_info, print_as_gui, should_i_do
# 
# from pkg_py.system_object.get_list_calculated import get_list_calculated
# from pkg_py.system_object.local_test_activate import LTA
# # from pkg_py.system_object.is_os_windows import is_os_windows
# 
# from pkg_py.system_object.performance_logic import ensure_seconds_measured, pk_measure_memory
# from pkg_py.system_object.state_via_context import SpeedControlContext
# from pkg_py.system_object.state_via_database import PkSqlite3DB
# # from pkg_py.system_object.print_red import print_red
# from pkg_py.system_object.alias_keyboard_map import alias_keyboard_map
# from pkg_py.system_object.color_map import COLORAMA_CODE_MAP
# from pkg_py.system_object.color_map import ColormaColorMap
# from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
# from pkg_py.system_object.directories import D_DESKTOP
# from pkg_py.system_object.directories import D_DOWNLOADS
# from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
# from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
# from pkg_py.system_object.directories import D_PKG_ARCHIVED
# from pkg_py.system_object.directories import D_PKG_PKL
# from pkg_py.system_object.directories import D_PKG_PY
# from pkg_py.system_object.directories import D_PKG_PY, D_PKG_ARCHIVED
# from pkg_py.system_object.directories import D_PKG_TXT
# from pkg_py.system_object.directories import D_PKG_TXT, D_PK_WORKING
# from pkg_py.system_object.directories import D_PK_FUNCTIONS_SPLIT
# from pkg_py.system_object.directories import D_PK_FUNCTIONS_SPLIT, D_PKG_ARCHIVED
# from pkg_py.system_object.directories import D_PK_WORKING
# from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS
# from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PKL
# from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PKL, D_PKG_PY
# from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS, D_PKG_PY
# from pkg_py.system_object.directories_reuseable import D_PROJECT
# from pkg_py.system_object.encodings import Encoding
# from pkg_py.system_object.etc import PK_UNDERLINE
# from pkg_py.system_object.etc import PkFilter
# from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
# from pkg_py.system_object.files import F_FFMPEG_EXE
# from pkg_py.system_object.files import F_HISTORICAL_PNX
# from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
# from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
# from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE, F_HISTORICAL_PNX
# from pkg_py.system_object.files import F_TEMP_TXT
# from pkg_py.system_object.map_massages import PkMessages2025
# from pkg_py.system_object.stamps import STAMP_ATTEMPTED
# from pkg_py.system_object.stamps import STAMP_DEBUG, STAMP_INTERACTIVE, STAMP_SUCCEEDED, STAMP_INFO, STAMP_TEST, STAMP_ERROR
# from pkg_py.system_object.stamps import STAMP_LIST, STAMP_TUPLE, STAMP_DICT, STAMP_SET
# from pkg_py.system_object.stamps import STAMP_PK_ENVIRONMENT_WITH_UNDERBAR
# from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
# from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED
# from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
# from pkg_py.refactor.ensure_keyboard_mouse_macro import PkMacroRoutines
# from pkg_py.refactor.pk_ensure_functions_splited import restore_workspace_from_latest_archive, split_by_top_level_def, backup_workspace
# from pkg_py.refactor.ensure_keyboard_mouse_macro import PkMacroRoutines
# from pkg_py.refactor.pk_ensure_modules_enabled_front import clean_import_block
# from pkg_py.workspace import ensure_pycharm_module_optimize
# from prompt_toolkit import prompt
# from prompt_toolkit import PromptSession
# from prompt_toolkit.completion import WordCompleter
# from prompt_toolkit.completion import WordCompleter, FuzzyCompleter
# from prompt_toolkit.shortcuts import CompleteStyle
# from prompt_toolkit.styles import Style
# from pympler import asizeof
# from pynput import mouse
# from PySide6.QtWidgets import QApplication
# from pytube import Playlist
# from queue import Queue, Empty
# from selenium.common.exceptions import ElementClickInterceptedException
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from seleniumbase import Driver
# from telegram import Bot
# from telegram import Bot, Update
# from telegram.ext import Application, MessageHandler, filters, CallbackContext
# from telethon import TelegramClient, events
# from tkinter import UNDERLINE
# from typing import List
# from typing import TypeVar
# from typing import TypeVar, List
# from urllib.parse import quote
# from urllib.parse import quote, urlparse
# from urllib.parse import unquote, urlparse, parse_qs
# from urllib.parse import urlparse
# from urllib.parse import urlparse, parse_qs, unquote
# from webdriver_manager.chrome import ChromeDriverManager
# from yt_dlp import YoutubeDL
# from zipfile import BadZipFile
# import ast
# import asyncio
# import browser_cookie3
# import calendar
# import chardet
# import clipboard
# import colorama
# import ctypes
# import cv2
# import datetime
# import easyocr
# import functools
# import glob
# import hashlib
# import importlib
# import inspect
# import ipdb
# import json
# import keyboard
# import logging
# import math
# import mutagen
# import mysql.connector
# import nest_asyncio
# import numpy as np
# import os
# import os, inspect
# import os.path
# import pandas as pd
# import paramiko
# import pickle
# import core_constants
# # import pkg_py.system_object.static_logic as system_object.static_logic
# import platform
# import psutil
# import pyaudio
# import pyautogui
# import pygetwindow
# import pyglet
# import pythoncom
# import pywintypes
# import random
# import random, math
# import re
# import requests
# import secrets
# import selenium.webdriver as webdriver
# import shlex
# import shutil
# import socket
# import speech_recognition as sr
# import sqlite3
# import statistics
# import string
# import subprocess
# import sys
# import tarfile
# import tempfile
# import threading
# import time
# import timeit
# import toml
# import toml  # toml:    쓰기 기능 추천
# import tomllib  # tomllib: 파싱/읽기 전용, binary 모드로 읽어야 하는 이유?
# import tqdm
# import traceback
# import undetected_chromedriver as uc
# import urllib
# import urllib.parse
# import uuid
# import webbrowser
# import win32api
# import win32com.client
# import win32con
# import win32con # pywin32

 # pywin32

# import winreg
# import yt_dlp
# import zipfile
# import zlib
# from pkg_py.functions_split.click_mouse_left_btn import click_mouse_left_btn
# from pkg_py.functions_split.does_text_bounding_box_exist_via_easy_ocr import does_text_bounding_box_exist_via_easy_ocr
# from pkg_py.functions_split.ensure_slept import ensure_slept