import zlib
import zipfile
import winreg
# import win32gui
# import win32gui
import win32com.client
import toml
import sys
import subprocess, time
import subprocess
import sqlite3
import secrets
import requests
import pyglet
import pygetwindow
import os.path
import json
import inspect
import importlib
import hashlib
import functools
import colorama
import calendar
from zipfile import BadZipFile
from urllib.parse import urlparse
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from pytube import Playlist
from pynput import mouse
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_800_print_util import print_red
from pkg_py.pk_system_layer_100_os import is_os_windows
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
from os import path
from functools import partial
from datetime import date
from collections import Counter
from bs4 import ResultSet
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_010_get_pnx_unix_style import get_pnx_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def build_aifw(vpc_data, config_remote_os):
    if vpc_data.vpc_type == 'no':
        # 도커 컨테이너 내부의 특정경로에서 build 해야함, 도커내부에 명령어를 수행해야함. cmd_to_remote_os 로 docker container 제어 가능한지 확인이 필요.
        d_packing_mode = vpc_data.vpc_aifw_packing_mode
        aifw_branch_n = vpc_data.vpc_aifw_branch_n  # 이 거 build 에서만 필요한 거 같은데
        if d_packing_mode == 1:
            # a2z내부개발용 # without packing mode
            # cd ~/Workspace/ai_framwork/build
            # cmake .. -DPACKING=1     # DPACKING = 0 이면  PACKING ? 확인필요
            todo('%%%FOO%%%')
        elif d_packing_mode == 0:
            # a2z외부차량탑재용 # with packing mode
            todo('%%%FOO%%%')
    elif vpc_data.vpc_type == 'nx':
        # cd ~/works/ai_framework/build
        # cmake --version
        # sudo apt-get install cmake
        # wget https://cmake.org/files/v3.16/cmake-3.16.3.tar.gz
        # tar -xvf cmake-3.16.3.tar.gz
        # cmake ..
        # make -j8  # 8 은 코어의 수 참조
        todo('%%%FOO%%%')
    elif vpc_data.vpc_type == 'xc':
        # build ai_framework
        # vscode/Remote Explorer/SSH/192.168.2.114/~/works/ai_framework/build
        # vscode/Remote Explorer/SSH/192.168.2.114/~/works/ai_framework/build make -j8
        todo('%%%FOO%%%')
