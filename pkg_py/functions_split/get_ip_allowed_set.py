

import zlib

import traceback
import tomllib
import timeit
import time
import tarfile
import sys
import speech_recognition as sr
import socket
import random
import pythoncom
import pyaudio
import numpy as np
import keyboard
import json
import inspect
import importlib
import colorama
import clipboard
import asyncio
from zipfile import BadZipFile
from pynput import mouse
from prompt_toolkit.styles import Style
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from os.path import dirname
from functools import partial as functools_partial
from functools import partial
from colorama import init as pk_colorama_init
from collections import Counter
from bs4 import ResultSet
from pkg_py.system_object.etc import PkFilter, PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style


def get_ip_allowed_set():
    ip_allowed_set = [
        get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_acu_it.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_a_side.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_b_side.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_test_02114.toml', initial_str=""),  # msi
        get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_test_10114.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_test_02124.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_test_10124.toml', initial_str=""),
        get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_galaxy_book_02076.toml', initial_str=""),
        'localhost',
        '10.10.10.114',
        '119.207.161.135',
    ]
    return ip_allowed_set
