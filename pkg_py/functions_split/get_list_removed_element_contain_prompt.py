# import win32gui
import win32con
import urllib
import tomllib
import subprocess
import socket
import requests
import psutil
import platform
import keyboard
import functools
import cv2
import colorama
import chardet
import browser_cookie3
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from typing import TypeVar, List
from telegram import Bot
from selenium.webdriver.chrome.service import Service
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.pk_system_object.Local_test_activate import LTA
from datetime import datetime
from Cryptodome.Random import get_random_bytes
from base64 import b64encode
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.is_os_windows import is_os_windows


def get_list_removed_element_contain_prompt(working_list, prompt):
    return [item for item in working_list if prompt not in item]
