import zlib
import zipfile
import yt_dlp
# import win32process
# import win32gui
import webbrowser
import toml
import timeit
import threading
import speech_recognition as sr
import shlex
import secrets
import re
import random
import pyglet
import pygetwindow
import pyautogui
import pyaudio
import psutil
import pickle
import os
import mysql.connector
import easyocr
import colorama
import clipboard
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote
from tkinter import UNDERLINE
from telegram import Bot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories import D_WORKING, D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_100_os import is_os_windows
from PIL import Image
from paramiko import SSHClient, AutoAddPolicy
from mutagen.mp3 import MP3
from gtts import gTTS
from datetime import datetime
from cryptography.hazmat.primitives import padding
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.pk_system_layer_100_Local_test_activate import LTA

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def rename_pnx_list_at_d(d_working, mode, with_walking, debug_mode=False):
    pk_print(working_str=rf'''d="{d_working}" mode="{mode}"  {'%%%FOO%%%' if LTA else ''}''')

    rename_pnxs_from_keywords_to_keyword_new_at_d(d=d_working, mode=mode, with_walking=with_walking)
    rename_pnxs_from_pattern_to_pattern_new_via_routines_at_d(d=d_working, mode=mode, with_walking=with_walking)
    rename_pnxs_from_keywords_to_keyword_new_at_d(d=d_working, mode=mode, with_walking=with_walking)
