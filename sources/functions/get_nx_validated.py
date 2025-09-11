import yt_dlp
import winreg

import tomllib
import toml
import sys
import sqlite3
import socket
import shlex
import random

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

from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_printed_once import ensure_printed_once
import logging
from sources.functions.ensure_list_written_to_f import ensure_list_written_to_f
from sources.functions.get_list_sorted import get_list_sorted

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.pk_etc import PkFilter
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_state_via_database import PkSqlite3DB
from sources.objects.pk_local_test_activate import LTA
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
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style

from sources.objects.pk_local_test_activate import LTA
import logging


def get_nx_validated(nx):
    nx = nx.strip()
    if any(char in nx for char in r'\/:*?"<>|'):
        logging.debug("Char not allowed in f_n/d_n. Retry.")
        raise
    return nx
