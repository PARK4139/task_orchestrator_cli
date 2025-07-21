import yt_dlp
import winreg
import webbrowser
import toml
import string
import speech_recognition as sr
# import pywin32
import mysql.connector
import math
import ipdb
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from prompt_toolkit.styles import Style
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from PIL import Image
from os import path
from moviepy import VideoFileClip
from datetime import datetime, time
from Cryptodome.Random import get_random_bytes
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from base64 import b64encode
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def get_list_leaved_element_contain_prompt(working_list, prompt):
    return [f for f in working_list if prompt in f]
