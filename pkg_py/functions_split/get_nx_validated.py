import yt_dlp
import winreg
# import win32gui
import tomllib
import toml
import sys
import sqlite3
import socket
import shlex
import random
# import pywin32
import pyglet
import pyaudio
import paramiko
import pandas as pd
import os.path
import numpy as np
import mysql.connector
import math
import hashlib
import functools
import clipboard
from urllib.parse import quote
from tkinter import UNDERLINE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from PySide6.QtWidgets import QApplication
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.get_list_sorted import get_list_sorted

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.etc import PkFilter
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories import D_WORKING
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from pkg_py.pk_system_object.local_test_activate import LTA
from os.path import dirname
from functools import partial as functools_partial
from functools import partial
from datetime import timedelta
from datetime import datetime
from datetime import date
from cryptography.hazmat.primitives import padding
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_nx_validated(nx):
    nx = nx.strip()
    if any(char in nx for char in r'\/:*?"<>|'):
        pk_print("Char not allowed in f_n/d_n. Retry.", print_color='red')
        raise
    return nx
