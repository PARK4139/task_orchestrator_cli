
import string
import sqlite3
import random
import pygetwindow
import pyautogui
import platform
import pickle
import paramiko
import os.path
import inspect
import importlib
import calendar
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from PySide6.QtWidgets import QApplication
from pynput import mouse

from sources.objects.pk_state_via_database import PkSqlite3DB


from os.path import dirname
from gtts import gTTS
from enum import Enum
from dirsync import sync
from datetime import date
from dataclasses import dataclass
from colorama import init as pk_colorama_init
from bs4 import BeautifulSoup
from base64 import b64encode
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
import logging


def truncate_tree(d_src):
    import inspect
    import os
    import shutil
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if os.path.exists(d_src):
        shutil.rmtree(d_src)
    if not os.path.exists(d_src):
        ensure_pnx_made(d_src, mode="d")
