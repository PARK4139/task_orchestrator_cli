import zipfile
import winreg
# import win32process
import win32con
import urllib.parse
import traceback
import tomllib
import toml
import sys
import subprocess
import sqlite3
import shlex
import secrets
import requests
import random
import pythoncom
import pyglet
import pygetwindow
import paramiko
import pandas as pd
import json
import inspect
import hashlib
import functools
import browser_cookie3
import asyncio
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from urllib.parse import urlparse, parse_qs, unquote
from typing import TypeVar, List
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from pytube import Playlist
from pynput import mouse
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_609_get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from os import path
from mutagen.mp3 import MP3
from moviepy import VideoFileClip
from functools import partial
from enum import Enum
from cryptography.hazmat.backends import default_backend
from Cryptodome.Cipher import AES
from concurrent.futures import ThreadPoolExecutor
from base64 import b64encode
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_007_get_list_calculated import get_list_calculated
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def get_categorized_f_dict_by_priority_ngrams(f_list, min_support, max_n, token_splitter_pattern):
    from collections import defaultdict, Counter
    ngram_counter = Counter()
    all_ngram_set = {}

    for f in f_list:
        all_ngram_list = get_all_ngram_list(f, max_n, token_splitter_pattern)
        all_ngram_set[f] = all_ngram_list
        ngram_counter.update(all_ngram_list)

    sorted_keywords = sorted(
        [k for k, v in ngram_counter.items() if v >= min_support and is_valid_ngram(k)],
        key=lambda x: -len(x.split())
    )

    categorized = defaultdict(list)
    assigned_files = set()

    for keyword in sorted_keywords:
        for f in f_list:
            if f in assigned_files:
                continue
            if keyword in all_ngram_set[f]:
                categorized[keyword].append(f)
                assigned_files.add(f)

    for f in f_list:
        if f not in assigned_files:
            categorized["기타"].append(f)
    return dict(categorized)
